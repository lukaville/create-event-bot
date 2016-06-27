from tinydb import TinyDB, Query


class TinyDBStore(object):
    def __init__(self):
        self.drafts_db = TinyDB('event_drafts.json')
        self.events_db = TinyDB('events.json')

    # Drafts
    def contains_draft(self, user_id):
        return self.drafts_db.contains(Query().user_id == user_id)

    def new_draft(self, user_id):
        if self.contains_draft(user_id):
            self.drafts_db.remove(Query().user_id == user_id)

        self.drafts_db.insert({
            'user_id': user_id,
            'current_field': 0,
            'event': {}
        })

    def update_draft(self, user_id, event, current_field):
        self.drafts_db.update({
            'user_id': user_id,
            'current_field': current_field,
            'event': event
        }, Query().user_id == user_id)

    def get_draft(self, user_id):
        return self.drafts_db.get(Query().user_id == user_id)

    def remove_draft(self, user_id):
        self.drafts_db.remove(Query().user_id == user_id)

    # Events
    def insert_event(self, event):
        event_id = self.events_db.insert(event)
        event['id'] = event_id
        return event

    def update_event(self, event):
        self.events_db.update(event, eids=[event.eid])

    def remove_event(self, event):
        self.events_db.remove(eids=[event['id']])

    def get_events(self, user_id, name=None):
        if name:
            return self.events_db.search((Query().user_id == user_id) & (Query().name.test(lambda v: name in v)))
        return self.events_db.search(Query().user_id == user_id)

    def get_event(self, event_id):
        return self.events_db.get(eid=int(event_id))
