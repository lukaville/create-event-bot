from telegram.ext import CommandHandler


def start_command(bot, update):
    bot.sendMessage(update.message.chat_id, text='...')


def help_command(bot, update):
    bot.sendMessage(update.message.chat_id, text='...')

command_handlers = [
    CommandHandler('start', start_command),
    CommandHandler('help', help_command)
]