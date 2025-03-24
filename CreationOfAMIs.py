# Automate the creation of Amazon Machine Images (AMIs) for EC2 instances to ensure system backups

import boto3

def create_ami(instance_id, ami_name):
    ec2 = boto3.client('ec2')
    ec2.create_image(InstanceId=instance_id, Name=ami_name, NoReboot=True)
    print(f"AMI {ami_name} created for instance {instance_id}")

# Example usage:
create_ami('i-1234567890abcdef0', 'my-ami-backup')