import discord_automessage
import schedule
import time
import random
import math

token = ""

intervals = [3, 4, 5, 6]
prefixs = ["sg!","\"","\"","\"","\""]
serverIds = [
    681211754654597242,
    450298280455176194,
    450298280455176194,
    450298280455176194,
    450298280455176194,
]
messages = [
    "club",
    "11",
    "swap 3 4",
    "swap 4 3",
    "show bellingham",
    "show hakimi",
    "show goretzka",
    "show sow",
    "show haaland",
    "show nkunku",
    "show valencia",
    "buy papin",
    "buy weah",
    "buy muller",
    "pack",
    "formation",
    "leaderboard votes",
    "leaderboard credits",
    "lb credits"
    ]
x = 0
t1 = time.time()
while 1:
    message = random.choice(messages)
    channel = random.randint(0, 4)
    interval = random.choice(intervals)
    discord_automessage.sendMessage(
        serverIds[channel],
        prefixs[channel] + message,
        token,
        log=False,
    )

    time.sleep(interval)
