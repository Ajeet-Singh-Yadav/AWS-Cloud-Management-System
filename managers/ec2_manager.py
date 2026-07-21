import boto3
from botocore.exceptions import ClientError
from utils.logger import logger

from config import *
from utils.printer import *
from utils.validator import *

# Create EC2 Client
ec2_client = boto3.client("ec2", region_name=REGION)

def get_instance_name(tags):

    if not tags:
        return "N/A"

    for tag in tags:

        if tag["Key"] == "Name":

            return tag["Value"]

    return "N/A"

def launch_instance():

    try:

        response = ec2_client.run_instances(

            ImageId=AMI_ID,

            InstanceType=INSTANCE_TYPE,

            KeyName=KEY_NAME,

            MinCount=1,

            MaxCount=1,

            TagSpecifications=[
                {
                    "ResourceType": "instance",

                    "Tags":[
                        {
                            "Key":"Name",
                            "Value":DEFAULT_TAG
                        }
                    ]
                }
            ]

        )

        instance_id = response["Instances"][0]["InstanceId"]

        success(f"\nEC2 Instance Created Successfully")

        logger.info(f"EC2 Instance {instance_id} launched successfully")

        info(f"Instance ID : {instance_id}")

    except ClientError as e:

        error(str(e))


from tabulate import tabulate

def describe_instances():

    try:

        response = ec2_client.describe_instances()

        table = []

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                table.append([

                    instance["InstanceId"],

                    get_instance_name(instance.get("Tags")),

                    instance["State"]["Name"],

                    instance["InstanceType"],

                    instance.get("PublicIpAddress","N/A"),

                    instance.get("PrivateIpAddress","N/A")

                ])

        print()

        print(tabulate(
            table,
            headers=[
                "Instance ID",
                "Name",
                "State",
                "Type",
                "Public IP",
                "Private IP"
            ],
            tablefmt="grid"
        ))

    except ClientError as e:

        error(str(e))



def start_instance():

    instance_id = get_instance_id()

    try:

        ec2_client.start_instances(

            InstanceIds=[instance_id]

        )

        success("Instance Started Successfully")

        logger.info(f"{instance_id} started")

    except ClientError as e:

        error(str(e))


def stop_instance():

    instance_id = get_instance_id()

    try:

        ec2_client.stop_instances(

            InstanceIds=[instance_id]

        )

        success("Instance Stopped Successfully")

        logger.info(f"{instance_id} stopped")

    except ClientError as e:

        error(str(e))


def reboot_instance():

    instance_id = get_instance_id()

    try:

        ec2_client.reboot_instances(

            InstanceIds=[instance_id]

        )

        success("Reboot Request Sent")

        logger.info(f"{instance_id} rebooted")

    except ClientError as e:

        error(str(e))


def terminate_instance():

    instance_id = get_instance_id()

    try:

        ec2_client.terminate_instances(

            InstanceIds=[instance_id]

        )

        success("Instance Terminated Successfully")

        logger.info(f"{instance_id} terminated")

    except ClientError as e:

        error(str(e))


def running_instances():

    response = ec2_client.describe_instances(

        Filters=[
            {
                "Name":"instance-state-name",

                "Values":["running"]
            }
        ]

    )

    print()

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            print(

                instance["InstanceId"],

                "-->",

                instance["State"]["Name"]

            )


def stopped_instances():

    response = ec2_client.describe_instances(

        Filters=[
            {
                "Name":"instance-state-name",

                "Values":["stopped"]
            }
        ]

    )

    print()

    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            print(

                instance["InstanceId"],

                "-->",

                instance["State"]["Name"]

            )


def ec2_menu():

    while True:

        heading("\n========= EC2 MANAGEMENT =========")

        print("""
1. Launch Instance
2. Describe Instances
3. Start Instance
4. Stop Instance
5. Reboot Instance
6. Terminate Instance
7. Running Instances
8. Stopped Instances
9. Back
""")

        choice = input("Enter Choice : ")

        if choice=="1":

            launch_instance()

        elif choice=="2":

            describe_instances()

        elif choice=="3":

            start_instance()

        elif choice=="4":

            stop_instance()

        elif choice=="5":

            reboot_instance()

        elif choice=="6":

            terminate_instance()

        elif choice=="7":

            running_instances()

        elif choice=="8":

            stopped_instances()

        elif choice=="9":

            break

        else:

            error("Invalid Choice")
