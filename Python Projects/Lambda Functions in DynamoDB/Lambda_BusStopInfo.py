from __future__ import print_function

import json
import boto3

print('Loading function')


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BusStopInfo')

    # print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['stop'])
    print("value2 = " + event['dayofweek'])

    response = table.get_item(  # This returns no data if key is not found
        Key={
            'stop': event['stop'],
            'dayofweek': event['dayofweek']
        }
        # attributes_to_get
    )

    try:
        item = response['Item']
    except:
        return "No results return (possible invalid bus stop code)!"

    result = "Description:" + item["description"] + \
             ", Total Board:" + str(item["totalboard"]) + \
             ", Total Alight:" + str(item["totalalight"])

    return result

# Curl commands
# curl -H "Content-Type: application/json" -X POST -d "{\"stop\":\"98011\",\"dayofweek\":\"SUNDAY\"}" https://7tubmgqkq3.execute-api.ap-northeast-1.amazonaws.com/testing/busstopinfo
# curl -H "Content-Type: application/json" -X POST -d "{\"stop\":\"96209\",\"dayofweek\":\"SUNDAY\"}" https://7tubmgqkq3.execute-api.ap-northeast-1.amazonaws.com/testing/busstopinfo
# {
#     "stop":"98011",
#     "dayofweek":"SUNDAY"
# }



