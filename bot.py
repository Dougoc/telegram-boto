# encoding: utf-8
import telegram
import logging
import subprocess
import os
import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler
from lxml import html
from telegram.ext import MessageHandler, Filters

updater = Updater(token='244002913:AAG_Omkgq7BJNOPWGIrXTd4fa9_SC7oiNvA')

dispatcher = updater.dispatcher

url_lero_lero = 'http://www.lerolero.com'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Ola, Como posso te ajudar?')

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

def frase(bot, update, args):
    page = requests.get(url_lero_lero)
    tree = html.fromstring(page.text)
    leia_frase = tree.xpath('//*[@id="frase_aqui"]/text()')[0]
    bot.sendMessage(chat_id=update.message.chat_id, text=leia_frase)

frase_handler = CommandHandler('frase', frase, pass_args=True)
dispatcher.add_handler(frase_handler)

def desconhecido(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Opa, nao entendi bem. Sera que vc pode repetir?')

desconhecido_handler = MessageHandler([Filters.command], desconhecido)
dispatcher.add_handler(desconhecido_handler)
