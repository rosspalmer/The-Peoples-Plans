
from json import JSONEncoder, dump, dumps, loads
from typing import Any

from pplans.data.models import *

DATA_MODELS = {
    AuthorData,
    EventData,
    EventNoteData,
    LocationData,
    RawMessageData,
}
MODEL_MAP = {cls.get_model_name(): cls for cls in DATA_MODELS}


def decode(model_name: str, json: str) -> SerializableData:

    if model_name not in MODEL_MAP:
        print('TODO - model not found exception')

    model_class = MODEL_MAP[model_name]
    data = loads(json, object_hook=model_class.json_object_hook)

    return data


class PPlansEncoder(JSONEncoder):

    def default(self, o: Any) -> Any:

        if o.__class__ in DATA_MODELS:
            return o.encode(o)

        return JSONEncoder.default(self, o)


def encode(data: SerializableData) -> str:
    return dumps(data, cls=PPlansEncoder)


def encode_stream(data: List[SerializableData], stream):
    dump(data, stream, cls=PPlansEncoder)
