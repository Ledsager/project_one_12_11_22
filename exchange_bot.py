from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater


async def command_exch(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(f'перевод валют')

async def command_help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(f'/exch - перевод валют\n/rate - курс валют\n/help\n')
