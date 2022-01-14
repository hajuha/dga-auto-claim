import discord_automessage
import schedule
import time

# def owo_hunt():
#     discord_automessage.sendMessage(901671756803227679, "owo hunt", log=False)
#     discord_automessage.sendMessage(901671756803227679, "owo battle", log=False)

def change_nickname():
    duration = int((time.time() - 1641840929)/60)
    discord_automessage.changeNickName(868041533503442984, str(duration) + " phút chưa claim được 85+")

schedule.every().minutes.do(change_nickname)

while 1:    
    schedule.run_pending()
    time.sleep(1)
