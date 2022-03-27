
import boto3

from collections import defaultdict
from os import environ
from typing import Dict

from pplans import decode, S3Data
from pplans.data.models import *


DATA_TYPES: Dict[str, SerializableData.__class__] = {
    'raw_message': RawMessageData,
    'event': EventData,
}
JSON_BUCKET = environ.get('JSON_BUCKET')

s3 = S3Data(boto3.client('s3'))


def insert_singles(data: List[SerializableData]):

    for d in data:
        s3.insert_data_single(JSON_BUCKET, d)


def insert_batches(batch_uid: str, data: List[SerializableData]):

    batch_map = defaultdict(list)
    for d in data:
        batch_map[d.get_model_name()].append(d)

    for name, batch in batch_map:
        s3.insert_data_batch(JSON_BUCKET, batch_uid, batch)


def handler(event, context):

    batch_uid = None
    if 'batch_uid' in event:
        batch_uid = event['batch_uid']

    if 'data' not in event:
        print("TODO - Exception data not defined")
    data = [decode(name, str(json).replace("'", '"')) for name, json in event['data']]

    if batch_uid is None:
        insert_singles(data)
    else:
        insert_batches(batch_uid, data)
