import time
import uuid

import boto3
import os
import base64
from botocore.exceptions import ClientError
import imghdr
import botocore
from dotenv import load_dotenv

load_dotenv()


class FileFolder:

    @classmethod
    def school(cls, name):
        return f"{name}/profile"

    @classmethod
    def parent_profile(cls, school_name, email):
        return f"{school_name}/parents/{email}/file-ab5619e7"

    @classmethod
    def student_profile(cls, school_name, email):
        return f"{school_name}/students/{email}/file-ab5619e7"

    @classmethod
    def teacher_profile(cls, school_name, email):
        return f"{school_name}/teachers/{email}/file-ab5619e7"

    @classmethod
    def admin_profile(cls, email):
        return f"admins/{email}"

    @classmethod
    def student_file(cls, school_name, email, file_name):
        return f"{school_name}/students/{email}/{file_name}", file_name

    @classmethod
    def project_file(cls, school_name, project_name, file_name):
        return f"{school_name}/projects/{project_name}/{file_name}", file_name

    @classmethod
    def learning_group_file(cls, school_name, learning_group_name, file_name):
        return f"{school_name}/learning_group/{learning_group_name}/{file_name}", file_name


class FileHandler:
    aws_access_key = os.environ.get("AWS_ACCESS_KEY")
    aws_secret_key = os.environ.get("AWS_SECRET_ACCESS")
    aws_cloudfront_distribution_id = os.environ.get("AWS_CLOUDFRONT_DISTRIBUTION_ID")
    bucket_name = "keyhub-folder"
    cloudfront_url = "https://d1xhar4wn7l1cd.cloudfront.net/"

    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name='us-east-2',
    )

    @staticmethod
    def extract_base64_data(file):
        if file.startswith("data:image/jpeg;base64,") or file.startswith("data:image/png;base64,") or file.startswith("data:image/jpg;base64,"):
            content_type = file.split(';')[0].split(':')[1]
            base64_encoded_data = file.split(',', 1)[1]
        else:
            base64_encoded_data = file
            decoded_data = base64.b64decode(base64_encoded_data)
            content_type = imghdr.what(None, h=decoded_data) or 'binary/octet-stream'

        # Ensure base64 data length is a multiple of 4
        missing_padding = len(base64_encoded_data) % 4
        if missing_padding != 0:
            base64_encoded_data += '=' * (4 - missing_padding)

        return content_type, base64_encoded_data

    @classmethod
    def upload_file(cls, file, file_path):

        try:
            content_type, base64_encoded_data = cls.extract_base64_data(file)
            decoded_image_data = base64.b64decode(base64_encoded_data)
            cls.s3.put_object(
                Bucket=cls.bucket_name,
                Key=file_path,
                Body=decoded_image_data,
                ContentType=str(content_type)  # Specify the content type as needed
            )

            # Generate a pre-signed URL for the uploaded image
            image_url = cls.get_file_url(str(file_path))
            return image_url, content_type
        except Exception as e:
            print(f"Failed to upload image: {e}")
            raise f"Image Error {e}"

    @classmethod
    def get_file_url(cls, file_name):
        try:
            # Generate a pre-signed URL for the file
            url = f"https://keyhub-folder.s3.us-east-2.amazonaws.com/{file_name}"
            response = url
            return response
        except Exception as e:
            print(f"Failed to upload file url: {e}")
            raise e

    @classmethod
    def delete_file(cls, file_name):
        try:
            cls.s3.delete_object(Bucket=cls.bucket_name, Key=file_name)
            return True
        except ClientError as e:
            print(f"Deletion failed: {e}")
            return False

    @classmethod
    def update_file(cls, file, file_name):
        # Deleting the old file and uploading the updated one
        try:
            if cls.delete_file(file_name):
                return cls.upload_file(file, file_name)
        except Exception as e:
            print("failed to upload file :: {}".format(e))
            raise e
