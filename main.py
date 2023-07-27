import boto3

def list_ec2_instances():
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # List all EC2 instances
    response = ec2.describe_instances()

    # Extract and print the instance details
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            state = instance['State']['Name']
            public_ip = instance.get('PublicIpAddress', 'N/A')
            private_ip = instance['PrivateIpAddress']
            print(f"Instance ID: {instance_id}")
            print(f"Instance Type: {instance_type}")
            print(f"State: {state}")
            print(f"Public IP: {public_ip}")
            print(f"Private IP: {private_ip}")
            print("")

# Usage example
list_ec2_instances()
print("Hello world")AKIATVSOCRUAGULLVMHO
