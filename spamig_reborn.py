from tkinter import E
from telethon import TelegramClient, events, sync
from colorama import Fore, Style, init
import rstr

init()

print(Fore.BLUE)
print("""
  ____                        _       
 / ___| _ __   __ _ _ __ ___ (_) __ _ 
 \___ \| '_ \ / _` | '_ ` _ \| |/ _` |
  ___) | |_) | (_| | | | | | | | (_| |
 |____/| .__/ \__,_|_| |_| |_|_|\__, |
       |_|                      |___/ 
                        Goofy ah selfbot spammer
""")

api_id = 
api_hash = ''

print(Fore.CYAN)

client = TelegramClient('session_name', api_id, api_hash)
client.start()

times = int(input("times: "))
text = input("Enter spam text: ")
trigger = input("Enter trigger text: ")
mode = "standart"

@client.on(events.NewMessage(pattern=trigger))
async def handler(event):
    for i in range(times+1):
        if (mode == "random"):
            await event.respond(rstr.xeger(r'[A-Z]\d[A-Z] \d[A-Z]\d'))
            print(Fore.GREEN + "Sended " + str(i) + " times")
        else:
            await event.respond(text)
            print(Fore.GREEN + "Sended " + str(i) + " times")


client.run_until_disconnected()