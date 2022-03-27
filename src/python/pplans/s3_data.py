
from io import StringIO
from json import dump
from typing import List

from pplans import encode
from pplans.data.models import SerializableData


class S3Data:

    def __init__(self, s3):
        self.s3 = s3

    def insert_data_single(self, bucket: str, data: SerializableData):

        self.s3.put_object(
            Body=encode(data),
            Bucket=bucket,
            Key=f'{data.get_model_name()}/{data.uid}.json'
        )

    def insert_data_batch(self, bucket: str, batch_uid: str, data: List[SerializableData]):

        models = {d.__class__ for d in data}
        if len(models) > 1:
            print('TODO - not all the same model type')
        data_model_name = list(models)[0]

        body = StringIO()
        dump([encode(d) for d in data], body)

        self.s3.put_object(
            Body=body,
            Bucket=bucket,
            Key=f'{data_model_name}/{batch_uid}.json'
        )
