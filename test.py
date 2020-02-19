import json

def lambda_handler(event, context):
    msg = 'helloPeter'
    return {
        "statusCode": 200,
        "body": json.dumps(msg)
    }