
from abc import ABC, abstractmethod
import datetime as dt
from json import JSONEncoder, loads
from typing import Any, Dict, List

DATE_FMT = '%Y-%m-%dT%H:%M:%S'


class SerializableData(ABC):

    def __init__(self, uid: str):
        self.uid = uid

    @abstractmethod
    def _get_encoder(self) -> JSONEncoder:
        pass

    @staticmethod
    @abstractmethod
    def get_model_name() -> str:
        pass

    @staticmethod
    @abstractmethod
    def json_object_hook(o: Dict) -> Any:
        pass

    def encode(self) -> str:
        return self._get_encoder().encode(self)


class DictEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__


class RawMessageData(SerializableData):

    def __init__(self, uid: str, author: str, text: str, created: str = None):
        super().__init__(uid)
        self.author = author
        self.text = text
        self.created = dt.datetime.now().strftime(DATE_FMT) if created is None else created

    @staticmethod
    def get_model_name() -> str:
        return 'raw_message'

    @staticmethod
    def json_object_hook(o: Dict) -> Any:
        return RawMessageData(**o)

    def _get_encoder(self) -> JSONEncoder:
        return DictEncoder()


class EventData(SerializableData):

    def __init__(self, uid: str, name: str, datetime: str,
                 location_uid: str, link: str, tags: List[str] = None):
        super().__init__(uid)
        self.name = name
        self.datetime = datetime
        self.location_uid = location_uid
        self.link = link
        self.tags = tags

    @staticmethod
    def get_model_name() -> str:
        return 'event'

    @staticmethod
    def json_object_hook(o: Dict) -> Any:
        return EventData(**o)

    def _get_encoder(self) -> JSONEncoder:
        return DictEncoder()


class Decoder:

    DATA_MODELS = {
        RawMessageData,
        EventData
    }

    def __init__(self):
        self._model_map = {model.get_model_name(): model for model in Decoder.DATA_MODELS}

    def run(self, model_name: str, json: str) -> SerializableData:

        if model_name not in self._model_map:
            print('TODO - model not found exception')

        model_class = self._model_map[model_name]

        data = loads(json, object_hook=model_class.json_object_hook)

        return data
