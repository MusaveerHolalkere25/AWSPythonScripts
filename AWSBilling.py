# Monitor AWS Billing Costs

import boto3

def get_aws_billing():
    ce = boto3.client('ce')
    response = ce.get_cost_and_usage(
        TimePeriod={'Start': '2023-01-01', 'End': '2023-01-31'},
        Granularity='MONTHLY',
        Metrics=['BlendedCost']
    )
    print(f"AWS Billing Cost: {response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']} USD")

# Example usage:
get_aws_billing()