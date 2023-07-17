import json
import boto3
import os
import json

iot_client = boto3.client('iot-data')
REDIRECT_URL= os.environ.get("REDIRECT_URL")
def lambda_handler(event, context):
    print(event)
    body=json.loads(event.get("body"))
    topic=body.get("topic")
    message=body.get("message")
    response = iot_client.publish(
        topic=topic,
        qos=1,
        payload=json.dumps(message)
    )
    print(response)
    
    return {
        'statusCode': 302,
        'headers': {
            'Location': REDIRECT_URL
        }
    }