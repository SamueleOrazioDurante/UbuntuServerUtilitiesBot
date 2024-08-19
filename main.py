
import telebot # telegram bot manager

# general utilities
import os
import time
import requests
import json
import datetime

# script
import tokenManager 

BOT_TOKEN = tokenManager.read_bot_token()
CHAT_ID = tokenManager.read_chat_id()

bot = telebot.TeleBot(BOT_TOKEN) # instance bot

# extra config for using local telegram API

#bot.log_out() # to log out from telegram base API (only first time)

#telebot.apihelper.API_URL = 'http://0.0.0.0:8080/bot{0}/{1}'
#telebot.apihelper.FILE_URL = 'http://0.0.0.0:8080'

@bot.message_handler(commands=['stats'])
def send_stats(message):
    bot.delete_message(message.chat.id, message.id)
    MESSAGE_ID = tokenManager.read_message_id()

    while True:
        msg = message_builder()
        if(MESSAGE_ID == None):
            message_bot = bot.send_message(CHAT_ID,msg)
            bot.pin_chat_message(CHAT_ID, message_bot.id)
            MESSAGE_ID = message_bot.id
            tokenManager.save_message_id(MESSAGE_ID)
        else:
            bot.edit_message_text(msg,CHAT_ID,MESSAGE_ID)
        time.sleep(5)

def message_builder():

    current_time = str(datetime.datetime.now())
    msg = "Server operativo! ✅ \n       📅  Data: "+ current_time

    webhook_url = tokenManager.read_webhook_data_url()
    body = requests.get(webhook_url) # trigger data webhook 
    data = json.loads(body.content) #get JSON data

    # add CPU info

    msg+="\nCPU:"
    msg+="\n        📈 Utilizzo: "+data["CPU_usage"]
    msg+="\n        🔥 Temperatura: "+data["CPU_temp"]

    # add RAM info

    msg+="\nRAM:"
    msg+="\n        📈 Utilizzo: "+data["RAM_usage"]+ " ("+data["RAM_available"]+" disponibili)"

    # add SSD info

    msg+="\nSSD:"
    msg+="\n        📈 Utilizzo: "+data["SSD_usage"]+ " ("+data["SSD_available"]+" disponibili)"
    msg+="\n        🔥 Temperatura: "+data["SSD_temp"]
    msg+="\n        ❤️ Health: "+data["SSD_health"]
    
    return msg


# non so come farlo  # edit: son riuscito a farlo
@bot.message_handler(commands=['wakeonlan', 'wol'])
def wakeOnLan(message):

    bot.delete_message(message.chat.id, message.id) # delete initial command

    webhook_url = tokenManager.read_webhook_wol_url() 
    requests.get(webhook_url) # trigger wol webhook 
    
    msg = bot.send_message(message.chat.id, "Wake On Lan del dispositivo! ") # response

    time.sleep(10)

    bot.delete_message(msg.chat.id, msg.id) # delete final command

@bot.message_handler(commands=['ping', 'pong'])
def ping(message):
    bot.delete_message(message.chat.id, message.id) # delete initial command

    # send one pkt
    hostname = message.text.split(" ")[1]
    print(hostname)
    response = os.system(f"ping -c 1 {hostname}")
    print(response)

    msg = None;

    #and then check the response...
    if response == 0:
        msg = (f"{hostname} is up! ✅ ({response} ms)")
    else:
        msg = (f"{hostname} is down! ❌ ")

    msg = bot.send_message(message.chat.id, msg) # response

    time.sleep(10)

    bot.delete_message(msg.chat.id, msg.id) # delete response

bot.polling() # bot start
