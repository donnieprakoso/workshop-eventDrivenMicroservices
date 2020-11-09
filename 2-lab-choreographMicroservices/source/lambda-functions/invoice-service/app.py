import time
import boto3
import json
import os
from datetime import datetime

'''
Lambda func for invoice service
'''
def save_to_db(id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    response = table.update_item(
        Key={'ID': id},
        UpdateExpression="set time_invoice_service=:sts",
        ExpressionAttributeValues={
            ':sts': datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        })

def lambda_handler(event, context):
    print(event)
    print('invoice_service is called')
    data = event['detail']['data'] 
    save_to_db(data['ID'])
    response = {'status':200}
    return response
