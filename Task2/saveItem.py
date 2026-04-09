import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')

def lambda_handler(event, context):
    # Handle body whether it's a string or already a dict
    body = event.get('body', '{}')
    if isinstance(body, str):
        body = json.loads(body)
    
    name = body.get('name', 'Unknown')
    item = {
        'id': str(uuid.uuid4()),
        'name': name
    }
    table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'message': 'Item saved', 'item': item})
    }
