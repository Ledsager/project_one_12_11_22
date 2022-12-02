from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("exch", callback_data='1'),
            InlineKeyboardButton("rate", callback_data='2'),
        ],
        [InlineKeyboardButton("Help", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def command_exch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    await update.message.reply_text(f'перевод валют')

async def command_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/exch - перевод валют\n/rate - курс валют\n/help\n')

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Sorry, I didn't understand that command.")
                            
