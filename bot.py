#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Create calendar events inline bot

import logging
import os

from telegram.ext import Updater

from commands import command_handlers
from inline import inline_handlers

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, err):
    logger.warn('Update "%s" caused error "%s"' % (update, err))


def main():
    updater = Updater(os.getenv('TELEGRAM_TOKEN'))

    dp = updater.dispatcher

    handlers = command_handlers + inline_handlers
    [dp.add_handler(handler) for handler in handlers]

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
