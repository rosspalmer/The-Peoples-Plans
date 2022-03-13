
import pytest

from pplans.data_models import RawEvent


class TestRawEvent:

    def test_encode(self):

        event = RawEvent("A-1", "ask@merch.com", "Do you know if you need stuff?")
        event_created = event.created

        answer = '{"uid": "A-1", "author": "ask@merch.com", "text": "Do you know if you need stuff?", ' \
                 f'"created": "{event_created}"' + '}'

        assert event.encode() == answer
