import boto3
from botocore.exceptions import ClientError

from utils.logger import logger

from config import *
from utils.printer import *

# Create DynamoDB Resource
dynamodb = boto3.resource("dynamodb", region_name=REGION)

# Create DynamoDB Client
dynamodb_client = boto3.client("dynamodb", region_name=REGION)


def list_tables():

    try:

        response = dynamodb_client.list_tables()

        heading("\n========= DYNAMODB TABLES =========\n")

        if len(response["TableNames"]) == 0:

            warning("No Tables Found")

            return

        for table in response["TableNames"]:

            print(table)

    except ClientError as e:

        error(str(e))


def create_table():

    table_name = input("Enter Table Name : ")

    try:

        table = dynamodb.create_table(

            TableName=table_name,

            KeySchema=[
                {
                    "AttributeName":"id",
                    "KeyType":"HASH"
                }
            ],

            AttributeDefinitions=[
                {
                    "AttributeName":"id",
                    "AttributeType":"S"
                }
            ],

            BillingMode="PAY_PER_REQUEST"

        )

        success("Table Created Successfully")

    except ClientError as e:

        error(str(e))


def insert_item():

    table_name = input("Enter Table Name : ")

    table = dynamodb.Table(table_name)

    student_id = input("Enter Student ID : ")

    name = input("Enter Name : ")

    city = input("Enter City : ")

    try:

        table.put_item(

            Item={

                "id":student_id,

                "Name":name,

                "City":city

            }

        )

        success("Item Inserted Successfully")

        logger.info(f"Inserted item {student_id} into {table_name}")

    except ClientError as e:

        error(str(e))


def read_item():

    table_name = input("Enter Table Name : ")

    table = dynamodb.Table(table_name)

    student_id = input("Enter Student ID : ")

    try:

        response = table.get_item(

            Key={

                "id":student_id

            }

        )

        item = response.get("Item")

        if item:

            print(item)

        else:

            warning("Item Not Found")

    except ClientError as e:

        error(str(e))


def update_item():

    table_name = input("Enter Table Name : ")

    table = dynamodb.Table(table_name)

    student_id = input("Enter Student ID : ")

    new_city = input("Enter New City : ")

    try:

        table.update_item(

            Key={

                "id":student_id

            },

            UpdateExpression="SET City=:c",

            ExpressionAttributeValues={

                ":c":new_city

            }

        )

        success("Item Updated Successfully")

    except ClientError as e:

        error(str(e))


def delete_item():

    table_name = input("Enter Table Name : ")

    table = dynamodb.Table(table_name)

    student_id = input("Enter Student ID : ")

    try:

        table.delete_item(

            Key={

                "id":student_id

            }

        )

        success("Item Deleted Successfully")

        logger.info(f"Deleted item {student_id} from {table_name}")

    except ClientError as e:

        error(str(e))


def delete_table():

    table_name = input("Enter Table Name : ")

    try:

        table = dynamodb.Table(table_name)

        table.delete()

        success("Table Deleted Successfully")

    except ClientError as e:

        error(str(e))


def scan_table():

    table_name = input("Enter Table Name : ")

    table = dynamodb.Table(table_name)

    try:

        response = table.scan()

        heading("\n========= TABLE DATA =========\n")

        for item in response["Items"]:

            print(item)

    except ClientError as e:

        error(str(e))


def dynamodb_menu():

    while True:

        heading("\n========== DYNAMODB ==========")

        print("""
1. List Tables
2. Create Table
3. Insert Item
4. Read Item
5. Update Item
6. Delete Item
7. Scan Table
8. Delete Table
9. Back
""")

        choice = input("Enter Choice : ")

        if choice == "1":

            list_tables()

        elif choice == "2":

            create_table()

        elif choice == "3":

            insert_item()

        elif choice == "4":

            read_item()

        elif choice == "5":

            update_item()

        elif choice == "6":

            delete_item()

        elif choice == "7":

            scan_table()

        elif choice == "8":

            delete_table()

        elif choice == "9":

            break

        else:

            error("Invalid Choice")