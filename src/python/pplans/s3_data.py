

from pplans.data.models import SerializableData


class S3Data:

    JSON_BUCKET = 'TODO'

    def __init__(self, s3):
        self.s3 = s3

    def insert_data(self, bucket: str, data: SerializableData):

        self.s3.put_object(
            Body=data.encode(),
            Bucket=bucket,
            Key=f'{data.get_model_name()}/{data.uid}.json'
        )
