import discord_automessage
import schedule
import time

def dga_claim():
    discord_automessage.sendMessage(888653476169666571,"dga!claim")
def dga_daily():
    discord_automessage.sendMessage(888653476169666571,"dga!daily")

schedule.every().hour.do(dga_claim)
schedule.every().day.at("21:30").do(dga_daily)
discord_automessage.sendMessage(888653476169666571,"This is a test message for @Yuhakez#0641 ")
discord_automessage.sendMessage(888653476169666571,"Auto claim start in")
time.sleep(1)
discord_automessage.sendMessage(888653476169666571,"3")
time.sleep(1)
discord_automessage.sendMessage(888653476169666571,"2")
time.sleep(1)
discord_automessage.sendMessage(888653476169666571,"1")
while 1:    
    schedule.run_pending()
    time.sleep(1)
