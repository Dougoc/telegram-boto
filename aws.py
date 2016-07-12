# encoding: utf-8
import bot
import boto

def frase(bot, update, args):
    page = requests.get(url_lero_lero)
    tree = html.fromstring(page.text)
    leia_frase = tree.xpath('//*[@id="frase_aqui"]/text()')[0]
    bot.sendMessage(chat_id=update.message.chat_id, text=leia_frase)

frase_handler = CommandHandler('frase', frase, pass_args=True)
dispatcher.add_handler(frase_handler)