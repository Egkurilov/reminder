
from datetime import datetime, timezone


class Message:
    def __init__(self, data):
        self._data = data

    @property
    def id(self):
        return self._data['update_id']

    @property
    def message_id(self):
        return self._data['message']['id']

    @property
    def from_id(self):
        return self._data['message_id']

    @property
    def is_bot(self):
        return self._data['message']['from']['is_bot']

    @property
    def first_name(self):
        return self._data['message']['from']['first_name']

    @property
    def last_name(self):
        return self._data['message']['from']['last_name']

    @property
    def username(self):
        return self._data['message']['from']['username']

    @property
    def date(self):
        return datetime.fromtimestamp(self._data['message']['date']) \
            .replace(tzinfo=timezone.utc)

    @property
    def text(self):
        return self._data['message']['text']

