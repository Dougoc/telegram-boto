import telegram
import logging
from telegram.ext import Updater

updater = Updater(token='244002913:AAG_Omkgq7BJNOPWGIrXTd4fa9_SC7oiNvA')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Ola, Como posso te ajudar?')

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()    

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

def desconhecido(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Opa, nao entendi bem. Sera que vc pode repetir?')

desconhecido_handler = MessageHandler([Filters.command], desconhecido)
dispatcher.add_handler(desconhecido_handler)