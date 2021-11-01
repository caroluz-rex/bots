import requests
import json,time
import random
from mytoken import getToken
#LOGIN#
url = "https://discord.com"

session = requests.Session()
session.get(url)
daDiscordCookies = session.cookies.get_dict()

headers = {
    'cookie': daDiscordCookies["__dcfduid"],
    'Content-Type': "application/json"
    }

daToken = getToken()

def createNonce():
    daNonce = ""
    for digit in range(1,16):
        daNonce += str(random.randint(0,9))
    return(daNonce)

def sendMessage(daChannelID, daMessage, log = True):
    headers = {
    'cookie': daDiscordCookies["__dcfduid"],
    'authorization': daToken,
    'Content-Type': "application/json"
    }

    payload ={"content": daMessage,
    "nonce": str(createNonce()),
    "tts": False}
    
    if log == True:
        print("Payload:"+str(payload))
    requests.request("POST", url+"/api/v9/channels/"+str(daChannelID)+"/messages", json = payload, headers = headers)
    time.sleep(.25)

def getMessages(daChannelID, daRange, log = True):
    headers = {
    'cookie': daDiscordCookies["__dcfduid"],
    'authorization': daToken,
    'Content-Type': "application/json"
    }
    if log == True:
        print(url+"/api/v9/channels/"+str(daChannelID)+"/messages")
    daChannelMessages = requests.request("GET", url+"/api/v9/channels/"+str(daChannelID)+"/messages", headers = headers)
    if log == True:
        print(daChannelMessages)
    data = json.loads(daChannelMessages.text)
    return(data[0:daRange])
def displayTyping(daChannelID, daDuration):
    times = round(daDuration/1)
    headers = {
    'cookie': daDiscordCookies["__dcfduid"],
    'authorization': daToken,
    'Content-Type': "application/json"
    }
    for interval in range(times):
        requests.request("POST", url+"/api/v9/channels/"+str(daChannelID)+"/typing", json = "", headers = headers)
        time.sleep(1)