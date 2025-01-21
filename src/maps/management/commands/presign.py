from django.core.management.base import BaseCommand

import boto3
from botocore.exceptions import ClientError
from django.conf import settings
import logging


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    Parameters:
    - bucket_name: string
    - object_name: string
    - expiration: Time in seconds for the presigned URL to remain valid (default: 1 hour)

    Returns:
    - Presigned URL as string or None if error occurs
    """
    s3_client = boto3.client(
        's3',
        region_name=settings.AWS_S3_REGION_NAME,  # Your region (fr-par, nl-ams, pl-waw)
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,  # Endpoint URL for your region
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    try:
        s3_client.head_object(Bucket=bucket_name, Key=object_name)
    except ClientError as e:
        logging.error(f"Object verification failed: {e}")
        return None

    try:

        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name,
                    'Key': object_name},
            ExpiresIn=expiration)
    except ClientError as e:
        print(f"Error: {e}")
        return None

    return response


class Command(BaseCommand):

    def handle(self, verbosity=0, **options):
        url = create_presigned_url(settings.AWS_BUCKET_NAME, "yy/xx.png", 120)
        if url:
            print(f"Download URL: {url}")
