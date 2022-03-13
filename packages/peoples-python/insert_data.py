
import boto3
from typing import Dict
from json import loads

from pplans.data_models import SerializableData, EventData, RawMessageData

DATA_TYPES: Dict[str, SerializableData.__class__] = {
    'raw_message': RawMessageData,
    'event': EventData,
}

S3_BUCKETS = {
    'prod': 'peoples-plans-json-prod',
    'stg': 'peoples-plans-json-stg'
}


s3 = boto3.client('s3')


def lambda_handler(event, context):

    if 'data_type' not in event:
        print("ERROR1 - FIXME")
    data_type = event['data_type']

    if data_type not in DATA_TYPES:
        print('ERROR2 - FIXME')
    data_class = DATA_TYPES[data_type]

    if 'json' not in event:
        print('ERROR3 - FIXME')
    json_data = event['json']

    # FIXME remove debug
    print('JSON DATA')
    print(json_data)

    data = loads(json_data, object_hook=data_class.json_object_hook)

    # FIXME remove debug
    print('CLASS')
    print(data)


