
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

    @staticmethod
    def encode(o: Any) -> Any:
        return {k: v for k, v in o.__dict__.items() if v is not None}


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


class EventNoteData(SerializableData):

    def __init__(self, uid: str, event_uid: str, author_uid: str, note: str, created: str = None):
        super().__init__(uid)
        self.event_uid = event_uid
        self.author_uid = author_uid
        self.note = note
        self.created = dt.datetime.now().strftime(DATE_FMT) if created is None else created

    @staticmethod
    def get_model_name() -> str:
        return 'event_note'

    @staticmethod
    def json_object_hook(o: Dict) -> Any:
        return EventNoteData(**o)


class LocationAddress:

    def __init__(self, street_number: str = None, street: str = None, unit: str = None,
                 city: str = None, state: str = None, zip_code: int = None, cross_street: str = None):
        self.street_number = street_number
        self.street = street
        self.unit = unit
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.cross_street = cross_street


class LocationGPS:

    def __init__(self, lat: float, long: float):
        self.lat = lat
        self.long = long


class LocationData(SerializableData):

    def __init__(self, uid: str, name: str, link: str,
                 address: LocationAddress = None, gps: LocationGPS = None):
        super().__init__(uid)
        self.name = name
        self.link = link
        self.address = address
        self.gps = gps

    @staticmethod
    def encode(o: Any) -> Any:

        data = {'uid': o.uid, 'name': o.name, 'link': o.link}
        if o.address is not None:
            data['address'] = super().encode(o.address)
        if o.gps is not None:
            data['gps'] = super().encode(o.gps)

        return data

    @staticmethod
    def get_model_name() -> str:
        return 'location'

    # @staticmethod
    # def json_object_hook(o: Dict) -> Any:
    #     address = LocationAddress(**o['address']) if 'address' in o else None
    #     gps = LocationAddress(**o['gps']) if 'gps' in o else None
    #     return LocationData(o['uid'], o['name'], o['link'], address, gps)

    @staticmethod
    def json_object_hook(o: Dict) -> Any:
        if 'lat' in o and 'long' in o:
            return LocationGPS(**o)
        elif 'uid' in o:
            return LocationData(**o)
        else:
            return LocationAddress(**o)


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
