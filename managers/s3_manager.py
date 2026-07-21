import boto3
from botocore.exceptions import ClientError
from utils.logger import logger

from config import *
from utils.printer import *
from utils.validator import *

# Create S3 Client
s3_client = boto3.client("s3", region_name=REGION)


def list_buckets():

    try:

        response = s3_client.list_buckets()

        heading("\n========= S3 BUCKETS =========\n")

        if len(response["Buckets"]) == 0:

            warning("No Bucket Found")

            return

        for bucket in response["Buckets"]:

            print(bucket["Name"])

    except ClientError as e:

        error(str(e))


def create_bucket():

    bucket_name = input("Enter Bucket Name : ")

    try:

        s3_client.create_bucket(

            Bucket=bucket_name,

            CreateBucketConfiguration={

                "LocationConstraint": REGION

            }

        )

        success("Bucket Created Successfully")

        logger.info(f"Bucket {bucket_name} created")

    except ClientError as e:

        error(str(e))


def upload_file():

    list_buckets()

    bucket_name = input("\nEnter Bucket Name : ")

    local_file = input("Enter File Path : ")

    try:

        s3_client.upload_file(

            local_file,

            bucket_name,

            local_file.split("/")[-1]

        )

        success("File Uploaded Successfully")

        logger.info(f"{local_file} uploaded to {bucket_name}")

    except ClientError as e:

        error(str(e))

    except FileNotFoundError:

        error("File Not Found")       


def download_file():

    bucket_name = input("Enter Bucket Name : ")

    object_name = input("Enter Object Name : ")

    download_path = f"downloads/{object_name}"

    try:

        s3_client.download_file(

            bucket_name,

            object_name,

            download_path

        )

        success("File Downloaded Successfully")

        logger.info(f"{object_name} downloaded from {bucket_name}")

        info(f"Saved In : {download_path}")

    except ClientError as e:

        error(str(e))


def list_objects():

    bucket_name = input("Enter Bucket Name : ")

    try:

        response = s3_client.list_objects_v2(

            Bucket=bucket_name

        )

        heading("\nObjects\n")

        if "Contents" not in response:

            warning("Bucket is Empty")

            return

        for obj in response["Contents"]:

            print(obj["Key"])

    except ClientError as e:

        error(str(e))


def delete_object():

    bucket_name = input("Enter Bucket Name : ")

    list_objects()

    object_name = input("\nEnter Object Name : ")

    try:

        s3_client.delete_object(

            Bucket=bucket_name,

            Key=object_name

        )

        success("Object Deleted Successfully")

        logger.info(f"{object_name} deleted from {bucket_name}")

    except ClientError as e:

        error(str(e))


def delete_bucket():

    bucket_name = input("Enter Bucket Name : ")

    try:

        s3_client.delete_bucket(

            Bucket=bucket_name

        )

        success("Bucket Deleted Successfully")

    except ClientError as e:

        error(str(e))


def s3_menu():

    while True:

        heading("\n========== AMAZON S3 ==========")

        print("""
1. List Buckets
2. Create Bucket
3. Upload File
4. Download File
5. List Objects
6. Delete Object
7. Delete Bucket
8. Back
""")

        choice = input("Enter Choice : ")

        if choice == "1":

            list_buckets()

        elif choice == "2":

            create_bucket()

        elif choice == "3":

            upload_file()

        elif choice == "4":

            download_file()

        elif choice == "5":

            list_objects()

        elif choice == "6":

            delete_object()

        elif choice == "7":

            delete_bucket()

        elif choice == "8":

            break

        else:

            error("Invalid Choice")