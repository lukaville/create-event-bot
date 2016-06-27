from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters

from store import TinyDBStore

FIELDS = [
    {
        'name': 'name',
        'message': 'Send me name of the event'
    },
    {
        'name': 'description',
        'message': 'Please send me the description of event (or /skip)',
        'required': False
    },
    {
        'name': 'date',
        'message': 'Please send me the date of event (e.g.: 10/25/16 12:20)'
    },
    {
        'name': 'place',
        'message': 'Please send me event duration in minutes (default — 60 minutes, /skip to set default value)',
        'required': False,
        'default': 60
    },
    {
        'name': 'place',
        'message': 'Please send me the place of event (or /skip)',
        'required': False
    },
]


def help_command(bot, update):
    bot.sendMessage(update.message.chat_id, text='...')


class CommandsModule(object):
    def __init__(self):
        self.handlers = [
            CommandHandler('start', self.start_command, pass_args=True),
            CommandHandler('help', help_command),
            MessageHandler([Filters.text], self.message)
        ]
        self.store = TinyDBStore()

    def start_command(self, bot, update, args):
        if args:
            if args[0] == 'new':
                user_id = update.message.from_user.id
                self.store.new_draft(user_id)
                bot.sendMessage(update.message.chat_id,
                                text="Let's create a new event. First, send me name of the event.")
        else:
            bot.sendMessage(update.message.chat_id, text="Hi!")

    def message(self, bot, update):
        user_id = update.message.from_user.id
        text = update.message.text
        draft = self.store.get_draft(user_id)

        if draft:
            event = draft['event']
            current_field = draft['current_field']
            field = FIELDS[current_field]

            event[field['name']] = text
            current_field += 1

            self.store.update_draft(user_id, event, current_field)

            if current_field <= len(FIELDS) - 1:
                bot.sendMessage(
                    update.message.chat_id,
                    text=FIELDS[current_field]['message']
                )
            else:
                event['user_id'] = user_id
                self.create_event(bot, update, event)

    def create_event(self, bot, update, event):
        self.store.insert_event(event)

        keyboard = [[InlineKeyboardButton(text='Send event', switch_inline_query=event['name'])], []]
        bot.sendMessage(
            update.message.chat_id,
            text="Event created!",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
        )

    def get_handlers(self):
        return self.handlers
