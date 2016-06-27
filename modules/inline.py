import datetime

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, Emoji
from telegram.ext import InlineQueryHandler, CallbackQueryHandler

from store import TinyDBStore


def create_event_payload(event):
    return 'abc'


def create_keyboard(event, user):
    buttons = [InlineKeyboardButton(
        text="Add to calendar",
        url='https://lukaville.github.com/create-event-bot/web/add.html#'+create_event_payload(event),
    )]

    if event.get('place'):
        buttons.append(InlineKeyboardButton(
            text="Map",
            url='https://maps.google.com/?q=' + event.get('place'),
        ))

    if 'users' in event and any(u['username'] == user['username'] for u in event['users']):
        buttons.append(InlineKeyboardButton(
            text="Exit",
            callback_data='ngo_' + str(event.eid)
        ))
    else:
        buttons.append(InlineKeyboardButton(
            text="Join",
            callback_data='go_' + str(event.eid)
        ))

    return [buttons, []]


def format_date(param):
    timestamp = int(param)
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime("%m/%d/%Y %H:%M")


def create_event_message(event, user):
    message_text = "*{name}*\n{date}\n".format(
        name=event['name'],
        date=format_date(event['date'])
    )

    if 'description' in event:
        message_text += Emoji.PAGE_WITH_CURL + ' _' + event['description'] + '_\n'

    if 'place' in event:
        message_text += Emoji.ROUND_PUSHPIN + ' ' + event['place'] + '\n'

    if 'users' in event and len(event['users']) > 0:
        message_text += '\nWill go: \n'
        for u in event['users']:
            message_text += '@' + u['username'] + ' (' + u['first_name'] + ' ' + u['last_name'] + ')\n'

    return message_text


class InlineModule(object):
    def __init__(self):
        self.handlers = [
            InlineQueryHandler(self.inline_query),
            CallbackQueryHandler(self.callback_handler)
        ]
        self.store = TinyDBStore()

    def callback_handler(self, bot, update):
        query = update.callback_query
        data = query.data
        user = query.from_user.__dict__

        (command, event_id) = tuple(data.split('_'))
        event = self.store.get_event(event_id)

        if command == 'go':
            event = self.add_user(event, user)

        if command == 'ngo':
            event = self.remove_user(event, user)

        bot.editMessageText(text=create_event_message(event, user),
                            inline_message_id=query.inline_message_id,
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=create_keyboard(event, user)),
                            parse_mode=ParseMode.MARKDOWN)

    def add_user(self, event, user):
        if not event.get('users'):
            event['users'] = []

        if not any(u['username'] == user['username'] for u in event['users']):
            event['users'].append(user)

        self.store.update_event(event)
        return event

    def remove_user(self, event, user):
        if not event.get('users'):
            return event

        event['users'].remove(user)

        self.store.update_event(event)
        return event

    def inline_query(self, bot, update):
        query = update.inline_query.query
        user_id = update.inline_query.from_user.id
        user = update.inline_query.from_user.__dict__

        results = []
        events = self.store.get_events(user_id, query)

        for event in events:
            keyboard = create_keyboard(event, user)
            result = InlineQueryResultArticle(id=event.eid,
                                              title=event['name'],
                                              description=format_date(event['date']),
                                              input_message_content=InputTextMessageContent(
                                                  create_event_message(event, user),
                                                  parse_mode=ParseMode.MARKDOWN
                                              ),
                                              reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard))
            results.append(result)

        bot.answerInlineQuery(
            update.inline_query.id,
            results=results,
            switch_pm_text='Create new event...',
            switch_pm_parameter='new'
        )

    def get_handlers(self):
        return self.handlers
