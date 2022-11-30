import os
from dotenv import load_dotenv

import logging

from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, ContextTypes

# from exchange_bot import *
# from viewer_bot import *
# from scrapper import db_action, get_data

load_dotenv()
secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():


    updater = Updater(token=secret_token)

    # updater.dispatcher.add_handler(CommandHandler("exch", command_exch))
    # updater.dispatcher.add_handler(CommandHandler("rate", command_rate))
    # updater.dispatcher.add_handler(CommandHandler("help", command_help))
    # app.add_handler(CommandHandler("hello", command_exch))


    print('Server run')
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater


def command_exch(update: Update, context: ContextTypes.DEFAULT_TYPE):

    update.message.reply_text(f'перевод валют')

def command_help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    update.message.reply_text(f'/exch - перевод валют\n/rate - курс валют\n/help\n') 


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater


def command_rate(update: Update, context: ContextTypes.DEFAULT_TYPE):

    update.message.reply_text(f'rate ready')   