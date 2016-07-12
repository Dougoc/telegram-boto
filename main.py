# encoding: utf-8
import bot
from bot import CommandHandler, updater, dispatcher, start

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()    
