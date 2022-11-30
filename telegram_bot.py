from dotenv import load_dotenv
import os
import logging

from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, ContextTypes

from exchange_bot import *
from viewer_bot import *
# from scrapper import db_action, get_data

load_dotenv()
secret_token = os.getenv('TOKEN')

def main():

    app = ApplicationBuilder().token(secret_token).build()

    

    app.add_handler(CommandHandler("exch", command_exch))
    app.add_handler(CommandHandler("rate", command_rate))
    app.add_handler(CommandHandler("help", command_help))
    # app.add_handler(CommandHandler(command, unknown))

    print('Server run')

    app.run_polling()

if __name__ == '__main__':
    main()