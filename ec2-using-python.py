import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

instance = ec2.create_instances(
    ImageId='ami-09e6f87a47903347c',  
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='princemittal', 
)

print(f"Launched instance with ID: {instance[0].id}")

instance = instance[0]
print("Waiting for instance to start...")
instance.wait_until_running()
instance.reload()
print(f"Public IP: {instance.public_ip_address}")
