
from abc import ABC, abstractmethod
import datetime as dt
from typing import Any, Dict, List

DATE_FMT = '%Y-%m-%dT%H:%M:%S'


class SerializableData(ABC):

    def __init__(self, uid: str):
        self.uid = uid

    @staticmethod
    @abstractmethod
    def get_model_name() -> str:
        pass

    @staticmethod
    @abstractmethod
    def json_object_hook(o: Dict) -> Any:
        pass


class RawMessageData(SerializableData):

    def __init__(self, uid: str, author_uid: str, text: str, created: str = None):
        super().__init__(uid)
        self.author_uid = author_uid
        self.text = text
        self.created = dt.datetime.now().strftime(DATE_FMT) if created is None else created

    @staticmethod
    def get_model_name() -> str:
        return 'raw_message'

    @staticmethod
    def json_object_hook(o: Dict) -> Any:
        return RawMessageData(**o)


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


class AuthorData(SerializableData):

    def __init__(self, uid: str, name: str, bot: bool):
        super().__init__(uid)
        self.name = name
        self.bot = bot

    @staticmethod
    def get_model_name() -> str:
        return 'author'

    @staticmethod
    def json_object_hook(o: Dict) -> Any:
        return AuthorData(**o)
