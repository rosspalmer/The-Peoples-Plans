from json import loads
from pplans.data.models import RawMessageData, EventData, DataPacket


class TestRawMessageData:

    def test_decode(self):

        msg_json = '{"uid":"B-5", "author":"a@b.co", "text": "hello peach", "created": "Y-M-D"}'
        msg = loads(msg_json, object_hook=RawMessageData.json_object_hook)

        assert msg.uid == "B-5"
        assert msg.author == "a@b.co"
        assert msg.text == "hello peach"
        assert msg.created == "Y-M-D"

    def test_encode(self):

        msg = RawMessageData("A-1", "ask@merch.com", "Do you know if you need stuff?")
        msg_created = msg.created

        answer = '{"uid": "A-1", "author": "ask@merch.com", "text": "Do you know if you need stuff?", ' \
                 f'"created": "{msg_created}"' + '}'

        assert msg.encode() == answer


class TestEventData:

    def test_decode(self):

        event_a_json = '{"uid": "E8t", "name": "A M8t", "datetime": "1900-02-03", "location_uid": ' \
                       '"hRe", "link": "hi.jack"}'
        event_b_json = '{"uid": "E8t", "name": "A M8t", "datetime": "1900-02-03", "location_uid": ' \
                       '"hRe", "link": "hi.jack", "tags": ["ok", "move"]}'

        event_a = loads(event_a_json, object_hook=EventData.json_object_hook)
        event_b = loads(event_b_json, object_hook=EventData.json_object_hook)

        assert event_a.uid == 'E8t'
        assert event_a.name == 'A M8t'
        assert event_a.datetime == '1900-02-03'
        assert event_a.location_uid == 'hRe'
        assert event_a.link == 'hi.jack'
        assert event_a.tags is None

        assert event_b.uid == 'E8t'
        assert event_b.name == 'A M8t'
        assert event_b.datetime == '1900-02-03'
        assert event_b.location_uid == 'hRe'
        assert event_b.link == 'hi.jack'
        assert event_b.tags == ['ok', 'move']

    def test_encode(self):

        event_a = EventData("E8t", "A M8t", "1900-02-03", "hRe", "hi.jack")
        event_b = EventData("E8t", "A M8t", "1900-02-03", "hRe", "hi.jack", ["ok", "move"])

        assert event_a.encode() == '{"uid": "E8t", "name": "A M8t", "datetime": "1900-02-03", "location_uid": ' \
                                   '"hRe", "link": "hi.jack", "tags": null}'
        assert event_b.encode() == '{"uid": "E8t", "name": "A M8t", "datetime": "1900-02-03", "location_uid": ' \
                                   '"hRe", "link": "hi.jack", "tags": ["ok", "move"]}'


class TestDataPacket:

    def test_encode(self):

        dp = DataPacket('bigPops', [
            RawMessageData('hello', 'world', 'foo', 'bar'),
            RawMessageData('more', 'generic', 'non', 'sense'),
            EventData('uyk', 'important-thing', '2018-02-03', 'here', 'www.com', ['A', 'B'])
        ])

        print(dp.encode())
