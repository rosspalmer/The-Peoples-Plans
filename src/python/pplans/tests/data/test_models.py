
from pplans.data.models import *
from pplans.data.serialize import decode, encode


class TestAuthorData:

    def test_decode(self):

        json = '{"uid": "ross@palmer.co", "name": "Ross Palmer", "bot": true}'
        author = decode('author', json)

        assert author.uid == 'ross@palmer.co'
        assert author.name == 'Ross Palmer'
        assert author.bot

    def test_encode(self):

        author = AuthorData('ross@palmer.co', 'Ross Palmer', True)

        assert encode(author) == '{"uid": "ross@palmer.co", "name": "Ross Palmer", "bot": true}'


class TestEventData:

    def test_decode(self):

        event_a_json = '{"uid": "E8t", "name": "A M8t", "datetime": "1900-02-03", "location_uid": ' \
                       '"hRe", "link": "hi.jack"}'
        event_b_json = '{"uid": "E8t", "name": "A M8t", "datetime": "1900-02-03", "location_uid": ' \
                       '"hRe", "link": "hi.jack", "tags": ["ok", "move"]}'

        event_a = decode(EventData.get_model_name(), event_a_json)
        event_b = decode(EventData.get_model_name(), event_b_json)

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

        assert encode(event_a) == '{"uid": "E8t", "name": "A M8t", "datetime": "1900-02-03", "location_uid": ' \
                                  '"hRe", "link": "hi.jack", "tags": null}'
        assert encode(event_b) == '{"uid": "E8t", "name": "A M8t", "datetime": "1900-02-03", "location_uid": ' \
                                  '"hRe", "link": "hi.jack", "tags": ["ok", "move"]}'


class TestEventNoteData:

    def test_decode(self):

        json = '{"uid":"what-this", "event_uid":"123", "author_uid":"a@b.co", ' \
               '"note": "hello peach", "created": "Y-M-D"}'
        data = decode(EventNoteData.get_model_name(), json)

        assert data.uid == 'what-this'
        assert data.event_uid == '123'
        assert data.author_uid == 'a@b.co'
        assert data.note == 'hello peach'
        assert data.created == 'Y-M-D'

    def test_encode(self):

        note = EventNoteData('what-this', '123', 'a@b.co', 'hello peach')
        note_created = note.created

        answer = '{"uid": "what-this", "event_uid": "123", "author_uid": "a@b.co", ' \
                 f'"note": "hello peach", "created": "{note_created}"' + '}'

        assert encode(note) == answer


class TestRawMessageData:

    def test_decode(self):

        json = '{"uid":"B-5", "author":"a@b.co", "text": "hello peach", "created": "Y-M-D"}'
        msg = decode(RawMessageData.get_model_name(), json)

        assert msg.uid == "B-5"
        assert msg.author == "a@b.co"
        assert msg.text == "hello peach"
        assert msg.created == "Y-M-D"

    def test_encode(self):

        msg = RawMessageData("A-1", "ask@merch.com", "Do you know if you need stuff?")
        msg_created = msg.created

        answer = '{"uid": "A-1", "author": "ask@merch.com", "text": "Do you know if you need stuff?", ' \
                 f'"created": "{msg_created}"' + '}'

        assert encode(msg) == answer

