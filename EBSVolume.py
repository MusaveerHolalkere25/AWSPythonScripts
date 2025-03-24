#Identify and delete unused Elastic Block Store (EBS) volumes to reduce costs.

import boto3

def delete_unused_ebs_volumes():
    ec2 = boto3.client('ec2')
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    for volume in volumes['Volumes']:
        ec2.delete_volume(VolumeId=volume['VolumeId'])
        print(f"Deleted volume: {volume['VolumeId']}")

# Example usage:
delete_unused_ebs_volumes()