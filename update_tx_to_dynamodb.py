import boto3
import time
dynamodb = boto3.client('dynamodb',region_name='us-west-1')


def dynamodb_transaction_hash_update(tx_dict):
    dynamodb.put_item(TableName='transactions', Item={'tx_hash':{"S": str(tx_dict['tx_hash'])},"total_value": {"N": str(tx_dict['total_value'])}\
            ,"timestamp":{"S":str(tx_dict['timestamp'])}})

def dynamodb_transaction_update(tx_dict):
    dynamodb.put_item(TableName='transaction', Item={'tx_hash':{"S": str(tx_dict['tx_hash'])}\
            ,"timestamp":{"S":str(tx_dict['timestamp'])},'inputs':{"S":str(tx_dict['txin'])},"outputs":{"S":str(tx_dict['txout'])}})
            

