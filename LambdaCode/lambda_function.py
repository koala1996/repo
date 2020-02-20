import boto3
import json

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    response = ec2.describe_availability_zones()
    msg = {'ec2':json.dumps(response), 'message':json.dumps('hello peter !!!')}

    return {"statusCode": 200, "body": json.dumps(msg)}
