import os
from telegram.ext import Updater, MessageHandler, Filters

def balas_pesan(update, context):
    pesan = update.message.text
    update.message.reply_text(f"Kamu mengirim: {pesan}")

TOKEN = os.getenv("TOKEN")
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

handler = MessageHandler(Filters.text, balas_pesan)
dispatcher.add_handler(handler)

updater.start_polling()
updater.idle()
