from tinydb import TinyDB


class TinyDBStore(object):
    def __init__(self, file='db.json'):
        self.db = TinyDB(file)

    def insert_event(self, event):
        event_id = self.db.insert(event)
        event['id'] = event_id

    def update_event(self, event):
        self.db.update(event, eids=[event['id']])

    def remove_event(self, event):
        self.db.remove(eids=[event['id']])
