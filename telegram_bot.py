# https://docs-python.ru/packages/biblioteka-python-telegram-bot-python/tipy-obrabotchikov/
from dotenv import load_dotenv
import os

import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
# import config
from exchange_bot import *
from viewer_bot import *
# from scrapper import db_action, get_data

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
secret_token = os.getenv('TOKEN')

def main():

    
    app = ApplicationBuilder().token(secret_token).build()



    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    app.add_handler(CommandHandler("exch", command_exch))
    app.add_handler(CommandHandler("rate", command_rate))
    app.add_handler(CommandHandler("help", command_help))

    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    print('Server run')

    app.run_polling()

if __name__ == '__main__':
    main()
