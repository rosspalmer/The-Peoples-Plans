
from abc import ABC, abstractmethod
import datetime as dt
from json import JSONEncoder
from typing import Any, Dict

DATE_FMT = '%Y-%m-%dT%H:%M:%S'


class SerializableData(ABC):

    @abstractmethod
    def _get_encoder(self) -> JSONEncoder:
        pass

    @staticmethod
    @abstractmethod
    def decode_function(o: Dict) -> Any:
        pass

    def encode(self) -> str:
        return self._get_encoder().encode(self)


class DictEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__


class RawMessage(SerializableData):

    def __init__(self, uid: str, author: str, text: str, created: str = None):
        self.uid = uid
        self.author = author
        self.text = text
        self.created = dt.datetime.now().strftime(DATE_FMT) if created is None else created

    @staticmethod
    def decode_function(o: Dict) -> Any:
        return RawMessage(o['uid'], o['author'], o['text'], o['created'])

    def _get_encoder(self) -> JSONEncoder:
        return DictEncoder()
