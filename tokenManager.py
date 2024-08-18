import os

def read_bot_token():

    #read bot token from config.py file
    BOT_TOKEN = None

    try:
        from config import BOT_TOKEN
    except:
        pass

    if len(BOT_TOKEN) == 0:
        BOT_TOKEN = os.environ.get('BOT_TOKEN')

    if BOT_TOKEN is None:
        raise ('Token for the bot must be provided (BOT_TOKEN variable)')
    return BOT_TOKEN

def read_chat_id():

    #read chat id from config.py file
    CHAT_ID= None

    try:
        from config import CHAT_ID
    except:
        pass

    if len(CHAT_ID) == 0:
        CHAT_ID = os.environ.get('CHAT_ID')

    if CHAT_ID is None:
        raise ('Token for the bot must be provided (CHAT_ID variable)')
    return CHAT_ID

def read_message_id():

    #read chat id from message_id file
    MESSAGE_ID = None

    try:
        file = open("message_id","r")
        MESSAGE_ID = file.read()
        file.close()
    except:
        pass

    return MESSAGE_ID

def save_message_id(MESSAGE_ID):
        
    file = open("message_id","w")
    file.write(str(MESSAGE_ID))
    file.close()

def read_webhook_wol_url():
    #read webhook wol url from config.py file
    WEBHOOK_WOL_URL= None

    try:
        from config import WEBHOOK_WOL_URL
    except:
        pass

    if len(WEBHOOK_WOL_URL) == 0:
        WEBHOOK_WOL_URL = os.environ.get('WEBHOOK_WOL_URL')

    if WEBHOOK_WOL_URL is None:
        raise ('Token for the bot must be provided (WEBHOOK_WOL_URL variable)')
    return WEBHOOK_WOL_URL

def read_webhook_data_url():
    #read webhook data url from config.py file
    WEBHOOK_DATA_URL= None

    try:
        from config import WEBHOOK_DATA_URL
    except:
        pass

    if len(WEBHOOK_DATA_URL) == 0:
        WEBHOOK_DATA_URL = os.environ.get('WEBHOOK_DATA_URL')

    if WEBHOOK_DATA_URL is None:
        raise ('Token for the bot must be provided (WEBHOOK_DATA_URL variable)')
    return WEBHOOK_DATA_URL
    