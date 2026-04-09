import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')

def lambda_handler(event, context):
    response = table.scan()
    items = response.get('Items', [])
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(items)
    }