import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from pyromod import listen
os.system("apt install git curl python3-pip ffmpeg -y")


API_ID = 10113557
API_HASH = "edd604444208db8ce6da5be78286187a"
TOKEN = "5680490457:AAHBb_s7dsGKA8y79B5Hbwkz_vjDNRCjBaw"

ZAID = Client("ZPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


@ZAID.on_message(filters.private & filters.command("start"))
async def hello(client: ZAID, message: Message):
    await message.reply("Hi, i am Parker Bot created by @pyrogrammers\nI can park your bot for maintenance mode.\nJust send ")

##Copy from here 

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@ZAID.on_message(filters.private & filters.command("Park"))
async def clone(bot: ZAID, msg: Message):
    chat = msg.chat
    #text = await msg.reply("Usage:\n\n /clone token")
    #cmd = msg.command
    phone = await ZAID.ask(chat.id, "Now send your bot token created from @botfather.")
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "handlers"})
        await client.start()
        idle()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Now Add Your Bot And Assistant @Amala_music_assistant_1 To Your Chat!\n\nThanks for Cloning.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!


ZAID.start()
idle()
