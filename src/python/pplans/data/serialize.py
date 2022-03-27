
from json import JSONEncoder, dumps, loads
from typing import Any

from pplans.data.models import SerializableData
from pplans.data.models import RawMessageData, EventData

DATA_MODELS_DICT = {
    RawMessageData,
    EventData
}
MODEL_MAP = {cls.get_model_name(): cls for cls in DATA_MODELS_DICT}


def decode(model_name: str, json: str) -> SerializableData:

    if model_name not in MODEL_MAP:
        print('TODO - model not found exception')

    model_class = MODEL_MAP[model_name]
    data = loads(json, object_hook=model_class.json_object_hook)

    return data


def is_dict_model(o: Any) -> bool:
    return True in {isinstance(o, cls) for cls in DATA_MODELS_DICT}


class PPlansEncoder(JSONEncoder):

    def default(self, o: Any) -> Any:

        if is_dict_model(o):
            return o.__dict__

        return JSONEncoder.default(self, o)


def encode(data: SerializableData) -> str:
    return dumps(data, cls=PPlansEncoder)
