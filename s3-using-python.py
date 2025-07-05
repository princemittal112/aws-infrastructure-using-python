# boto3 -> used to do AWS tasks using python

import uuid
import os
import boto3
import botocore.exceptions

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = response.get('Buckets', [])

    if not buckets:
        print("No buckets found.")
    else:
        print("S3 Buckets:")
        for bucket in buckets:
            print(f"- {bucket['Name']}")

# Call the function
list_s3_buckets()

# create s3 bucket in aws using python -> versioning enabled and sample file uploaded
def create_bucket():
    s3 = boto3.client('s3')
    region = boto3.session.Session().region_name

    name = input("Enter bucket name (leave empty to auto-generate): ").strip()
    if not name:
        name = f"bucket-{uuid.uuid4().hex[:10]}"
        print(f"Using generated bucket name: {name}")

    if region == 'us-east-1':
        s3.create_bucket(Bucket=name)
    else:
        s3.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
    print(f"Bucket '{name}' created in region {region}")

    # Enable versioning
    s3.put_bucket_versioning(
        Bucket=name,
        VersioningConfiguration={'Status': 'Enabled'}
    )

    # Upload a sample file
    filename = "sample.txt"
    with open(filename, "w") as f:
        f.write("Hello from Python and S3!")

    s3.upload_file(filename, name, filename)
    print(f"Uploaded '{filename}' to bucket '{name}'")

    os.remove(filename)

create_bucket()
