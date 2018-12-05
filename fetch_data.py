import requests
import json
from datetime import datetime
import arrow
import boto3

def get_latest_block_info():
    response = {}
    r = requests.get('https://blockchain.info/latestblock')
    r = json.loads(r.text)
    response['time']=(arrow.get(r['time']).to('local').format())
    response['hash'] = r['hash']
    response['block_index'] = r['block_index']
    return response

def get_single_block(block_hash):
    response = {}
    r = requests.get('https://blockchain.info/rawblock/' + str(block_hash))
    r = json.loads(r.text)
    response['hash'] = block_hash
    response['prev_block'] = r['prev_block']
    response['height'] = r['height']
    response['block_index'] = r['block_index']
    response['time'] = r['time']
    return response

def get_balance(address):
    response = {}
    r = requests.get('https://blockchain.info/balance?active=' + str(address))
    r = json.loads(r.text)
    response['final_balance'] = r[address]['final_balance']
    response['n_tx'] = r[address]['n_tx']
    response['total_received'] = r[address]['total_received']
    return response
    
def get_amount_in_usd():
    response = {}
    r = requests.get('https://blockchain.info/ticker')
    r = json.loads(r.text)
    response['last'] = r['USD']['last']
    response['buy'] = r['USD']['buy']
    response['sell'] = r['USD']['sell']
    return response

def convert_usd_to_btc(amount):
    response = requests.get('https://blockchain.info/tobtc?currency=USD&value=' + str(amount))
    return response.text

def fetch_transaction(tx_hash):
    dynamodb = boto3.client('dynamodb',region_name='us-west-1')
    response = dynamodb.get_item(TableName='transaction', Key={'tx_hash':{'S':str(tx_hash)}})
    if 'Item' in response:
        return response
    else:
        return "The Transaction not in the Database"







# print get_latest_block_info()
# 0000000000000000002f25644ca67a3051dc436a5acd0b7a84323cf0cdeb72e4
# print get_single_block('0000000000000000002f25644ca67a3051dc436a5acd0b7a84323cf0cdeb72e4')
# 0000000000000000002f25644ca67a3051dc436a5acd0b7a84323cf0cdeb72e4
# print get_balance('14Bag7dawf3v78hnQf4XKKd1nVAzY27pdf')
# print get_amount_in_usd()
# print convert_usd_to_btc(500)

print fetch_transaction('010690d5372594e88914968bb003c4cf33424b75f8a7d3355d7d966b6daf69e')