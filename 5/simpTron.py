import json,time
import random
from config import getScope, getMisc
import discAutoMsg.discord_automessage as discAutoMsg

channelIDtoMsg = getScope()
msgAsReply,msgPingReply = getMisc()

while True:
    lines = open('base.txt').read().splitlines()
    for channelID in list(channelIDtoMsg.keys()):
        myline = random.choice(lines)
        discAutoMsg.sendMessage(channelID, myline)
        time.sleep(random.randrange(2,20,1))
    time.sleep(random.randrange(30,100,6))