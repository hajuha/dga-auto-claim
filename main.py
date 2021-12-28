import discord_automessage
import schedule
import time

def dga_claim():
    discord_automessage.sendMessage(888653476169666571, "dga!claim", log=False)
    print("Auto claimed at ", time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
def dga_daily():
    discord_automessage.sendMessage(888653476169666571,"dga!daily")
    print("Auto daily at ", time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    
def dga_spam():
    discord_automessage.sendMessage(888653476169666571,"dga!11")

schedule.every(61).minutes.do(dga_claim)
schedule.every(1441).minutes.do(dga_daily)
discord_automessage.sendMessage(888653476169666571, "Test", log=False)

while 1:    
    schedule.run_pending()
    time.sleep(1)
