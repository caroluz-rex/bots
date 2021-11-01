import time
import random
from config import getScope
import discAutoMsg.discord_automessage as discAutoMsg

channelIDtoMsg = getScope()

while True:
    lines = open('base.txt').read().splitlines()
    for channelID in list(channelIDtoMsg.keys()):
        myline = random.choice(lines)
        discAutoMsg.displayTyping(channelID, 5)
        discAutoMsg.sendMessage(channelID, myline)
        time.sleep(random.randrange(2,20,1))
    time.sleep(random.randrange(30,60,6))