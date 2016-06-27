from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import InlineQueryHandler, CallbackQueryHandler

from store import TinyDBStore


def create_keyboard(event, user_name):
    add_to_calendar_button = InlineKeyboardButton(
        text="Add to calendar",
        url='http://google.com/',
    )

    if 'users' in event and user_name in event['users']:
        go_button = InlineKeyboardButton(
            text="I'm not going",
            callback_data='ngo_' + str(event.eid)
        )
    else:
        go_button = InlineKeyboardButton(
            text="I'm going",
            callback_data='go_' + str(event.eid)
        )

    return [[add_to_calendar_button, go_button], []]


def create_event_message(event, user_name):
    message_text = "*{name}*\n{date}\n".format(
        name=event['name'],
        date=event['date']
    )

    if 'description' in event:
        message_text += event['description'] + '\n'

    if 'place' in event:
        message_text += event['place'] + '\n'

    if 'users' in event and len(event['users']) > 0:
        message_text += 'Users: '
        for user in event['users']:
            message_text += '@' + user + ' '

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
        user_name = query.from_user.username

        (command, event_id) = tuple(data.split('_'))
        event = self.store.get_event(event_id)

        if command == 'go':
            event = self.add_user(event, user_name)

        if command == 'ngo':
            event = self.remove_user(event, user_name)

        bot.editMessageText(text=create_event_message(event, user_name),
                            inline_message_id=query.inline_message_id,
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=create_keyboard(event, user_name)),
                            parse_mode=ParseMode.MARKDOWN)

    def add_user(self, event, user_name):
        if not event.get('users'):
            event['users'] = []

        if user_name not in event['users']:
            event['users'].append(user_name)

        self.store.update_event(event)
        return event

    def remove_user(self, event, user_name):
        if not event.get('users'):
            return event

        event['users'].remove(user_name)

        self.store.update_event(event)
        return event

    def inline_query(self, bot, update):
        query = update.inline_query.query
        user_id = update.inline_query.from_user.id
        user_name = update.inline_query.from_user.username

        results = []
        events = self.store.get_events(user_id, query)

        for event in events:
            keyboard = create_keyboard(event, user_name)
            result = InlineQueryResultArticle(id=event.eid,
                                              title=event['name'],
                                              description=event['date'],
                                              input_message_content=InputTextMessageContent(
                                                  create_event_message(event, user_name),
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
