
from abc import ABC, abstractmethod
import datetime as dt
from json import dumps, JSONDecoder, JSONEncoder
from typing import Any


DATE_FMT = '%Y-%m-%dT%H:%M:%S'


class SerializableData(ABC):

    # @abstractmethod
    # def _get_decoder(self) -> JSONDecoder:
    #     pass
    #
    @abstractmethod
    def _get_encoder(self) -> JSONEncoder:
        pass

    def encode(self) -> str:
        return self._get_encoder().encode(self)


class DictEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__


class RawEvent(SerializableData):

    def __init__(self, uid: str, author: str, text: str):
        self.uid = uid
        self.author = author
        self.text = text
        self.created = dt.datetime.now().strftime(DATE_FMT)

    def _get_encoder(self) -> JSONEncoder:
        return DictEncoder()
