#pip install boto, boto3
import boto3  #http://boto.cloudhackers.com/en/latest/dynamodb2_tut.html (boto is a Python interface to Amazon Web Services)
import boto.dynamodb
import json

#connect to dynamo db, http://boto3.readthedocs.io/en/latest/guide/configuration.html
dynamodb = boto3.resource(
    'dynamodb',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='ap-northeast-1'
)

#http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html#DDB-CreateTable-request-AttributeDefinitions
#DynamoDB is schemaless. You only need to specify key schema. Any other attributes can be added in later. Anything in attributes definition must be in key schema.
table = dynamodb.create_table(
    TableName='BusStopInfo',
    KeySchema=[ #Specify the primary key
        {
            'AttributeName': 'stop',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'dayofweek',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'stop',
            'AttributeType': 'S'
        }
        ,
        {
            'AttributeName': 'dayofweek',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table = dynamodb.create_table(
    TableName='NetOnBoard',
    KeySchema=[ #Specify the primary key
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'direction',
            'KeyType': 'RANGE'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
        ,
        {
            'AttributeName': 'direction',
            'AttributeType': 'N'
        },
    ],
    # Testing https://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html#DynamoDB.ServiceResource.create_table
    # LocalSecondaryIndexes=[
    #     {
    #         'IndexName': 'dayofweek_direction',
    #         'KeySchema': [
    #             {
    #                 'AttributeName': 'dayofweek',
    #                 'KeyType': 'HASH'
    #             },
    #         ],
    #         'Projection': {
    #             'ProjectionType': 'KEYS_ONLY'
    #
    #         }
    #     },
    # ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
