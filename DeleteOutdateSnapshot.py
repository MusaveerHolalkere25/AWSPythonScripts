# Delete outdated snapshots to save storage costs:

import boto3

def cleanup_snapshots(retention_days=30):
    ec2 = boto3.client('ec2')
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
    for snapshot in snapshots:
        if (snapshot['StartTime']).days > retention_days:
            ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
            print(f"Deleted snapshot {snapshot['SnapshotId']}")

cleanup_snapshots()