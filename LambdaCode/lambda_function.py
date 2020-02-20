import boto3
import json

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    msg = 'helloToto'
    return {
        "statusCode": 200,
        "body": {
                "ec2" : json.dumps(response),
                "message" : json.dumps(msg)
        }
    }
