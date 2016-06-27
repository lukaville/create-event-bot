from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import InlineQueryHandler, CallbackQueryHandler


def create_keyboard(event):
    add_to_calendar_button = InlineKeyboardButton(
        text="Add to calendar",
        url='http://google.com/',
    )

    go_button = InlineKeyboardButton(
        text="I'm going",
        callback_data='go_' + event['id']
    )

    return [[add_to_calendar_button, go_button], []]


def callback_handler(bot, update):
    query = update.callback_query
    data = query.data
    user_name = query.from_user.id

    bot.editMessageText(text='Changed value!',
                        inline_message_id=query.inline_message_id,
                        reply_markup=InlineKeyboardMarkup(inline_keyboard=create_keyboard({
                            'id': str(uuid4())
                        })),
                        parse_mode=ParseMode.MARKDOWN)


def inline_query(bot, update):
    query = update.inline_query.query

    message = InputTextMessageContent(
        '*Встреча*\n12/12/16',
        parse_mode=ParseMode.MARKDOWN
    )

    keyboard = create_keyboard({
        'id': str(uuid4())
    })

    result = InlineQueryResultArticle(id=uuid4(),
                                      title='Create event',
                                      description='01/02/2015',
                                      input_message_content=message,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard))

    bot.answerInlineQuery(update.inline_query.id, results=[result])


inline_handlers = [
    InlineQueryHandler(inline_query),
    CallbackQueryHandler(callback_handler)
]
