
import pytest

from json import loads
from pplans.data_models import RawEvent


class TestRawEvent:

    def test_decode(self):

        event_json = '{"uid":"B-5", "author":"a@b.co", "text": "hello peach", "created": "Y-M-D"}'
        event = loads(event_json, object_hook=RawEvent.decode_function)

        assert event.uid == "B-5"
        assert event.author == "a@b.co"
        assert event.text == "hello peach"
        assert event.created == "Y-M-D"

    def test_encode(self):

        event = RawEvent("A-1", "ask@merch.com", "Do you know if you need stuff?")
        event_created = event.created

        answer = '{"uid": "A-1", "author": "ask@merch.com", "text": "Do you know if you need stuff?", ' \
                 f'"created": "{event_created}"' + '}'

        assert event.encode() == answer
