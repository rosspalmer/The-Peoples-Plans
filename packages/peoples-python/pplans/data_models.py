
from abc import ABC, abstractmethod
import datetime as dt
from json import JSONEncoder
from typing import Any, Dict, List

DATE_FMT = '%Y-%m-%dT%H:%M:%S'


class SerializableData(ABC):

    @abstractmethod
    def _get_encoder(self) -> JSONEncoder:
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
        self.uid = uid
        self.author = author
        self.text = text
        self.created = dt.datetime.now().strftime(DATE_FMT) if created is None else created

    @staticmethod
    def json_object_hook(o: Dict) -> Any:
        return RawMessageData(**o)

    def _get_encoder(self) -> JSONEncoder:
        return DictEncoder()


class EventData(SerializableData):

    def __init__(self, uid: str, name: str, datetime: str,
                 location_uid: str, link: str, tags: List[str] = None):
        self.uid = uid
        self.name = name
        self.datetime = datetime
        self.location_uid = location_uid
        self.link = link
        self.tags = tags

    @staticmethod
    def json_object_hook(o: Dict) -> Any:
        return EventData(**o)

    def _get_encoder(self) -> JSONEncoder:
        return DictEncoder()
