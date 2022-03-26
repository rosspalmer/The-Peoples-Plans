
import boto3

from os import environ
from typing import Dict

from pplans import Decoder, S3Data
from pplans.data_models import SerializableData, EventData, RawMessageData


DATA_TYPES: Dict[str, SerializableData.__class__] = {
    'raw_message': RawMessageData,
    'event': EventData,
}
JSON_BUCKET = environ.get('JSON_BUCKET')

s3 = S3Data(boto3.client('s3'))


def handler(event, context):

    if 'model_name' not in event:
        print("ERROR1 - FIXME")
    model_name = event['model_name']

    if 'json' not in event:
        print('ERROR3 - FIXME')
    json = str(event['json']).replace("'", '"')

    data = Decoder().run(model_name, json)

    s3.insert_data(JSON_BUCKET, data)
