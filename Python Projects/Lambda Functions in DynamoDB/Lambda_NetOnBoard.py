from __future__ import print_function

import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

print('Loading function')

from __future__ import print_function
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

print('Loading function')


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('NetOnBoard')

    response = table.scan(
        FilterExpression=Attr('dayofweek').eq(event['dayofweek']) & Attr('direction').eq(event['direction'])
    )

    try:
        items = (response['Items'])
    except:
        return "No results return! (dayofweek = 'SUNDAY' | 'WEEKDAY', direction = 0 | 1)"

    items.sort(key=lambda items: items["seq"])  # This order the items by seq
    print(items)

    # Calculate NetOnBoard
    netOnBoard = 0
    result = ""
    listResult = []
    for item in items:
        personboard = int(item["personboard"])
        personalight = int(item["personalight"])

        netOnBoard = netOnBoard + personboard
        if item["seq"] != 0:  # Add all except first bus stop
            netOnBoard = netOnBoard - personalight

        # print("At bus stop " + item["stop"] + ", " + str(item["personboard"]) + " board the bus and " + str(item["personalight"]) + " alight the bus. NetOnBoard: " + str(netOnBoard))
        # t = (item["seq"], item["direction"], + item["stop"],netOnBoard)

        result = "(Seq:" + str(item["seq"]) + ", Direction:" + str(item["direction"]) + ", Stop:" + str(
            item["stop"]) + ", NetOnBoard:" + str(netOnBoard) + ")"
        listResult.insert(len(listResult), result)

    return listResult

# Curl commands
# curl -H "Content-Type: application/json" -X POST -d "{\"dayofweek\":\"SUNDAY\",\"direction\":0}" https://7tubmgqkq3.execute-api.ap-northeast-1.amazonaws.com/testing/netonboard -o "file1.txt"
# curl -H "Content-Type: application/json" -X POST -d "{\"dayofweek\":\"WEEKDAY\",\"direction\":1}" https://7tubmgqkq3.execute-api.ap-northeast-1.amazonaws.com/testing/netonboard
# {
#   "dayofweek": "SUNDAY",
#   "direction": 1
# }