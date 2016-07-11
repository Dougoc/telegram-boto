import telegram
import logging
import time
import argparse

bot = telegram.Bot(token = 'xxx')
chat_id = bot.getUpdates()[-1].message.chat_id

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater.start_polling()

def foo():
    updates = bot.getUpdates()
    #   print(updates[-1].message.text)
    lastmessage = (updates[-1].message.text)
    if lastmessage == 'Boto' or 'boto':
        print('Estamos aqui para ajudar!')


    else:
        print('Por favor, digite um comando')
def run():
    while True:
        time.sleep(5)
        foo()

if __name__ == '__main__':
    run()


if lastmessage == help:
    print('Opa')    





