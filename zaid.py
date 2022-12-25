import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from pyromod import listen
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

API_ID = 10113557
API_HASH = "edd604444208db8ce6da5be78286187a"
TOKEN = "5533358298:AAGX817ACmIMJHYPUf3VR7Ul08aVcZ6byxs"
LOGS = "-1005846633"

ZAID = Client("ZPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


@ZAID.on_message(filters.private & filters.command("start"))
async def hello(client: ZAID, message: Message):
    await message.reply("Hii, i can your park your bot without using any server\nJust send `/park bot_token`, that's all.")

##Copy from here 

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@ZAID.on_message(filters.private & filters.command("clone"))
async def clone(bot: ZAID, msg: Message):
    chat = msg.chat
    text = await msg.reply("Send /clone with your bot token.\nYou can get your bot token from @botfather\n\ne.g. `/clone bot_token`.")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("⏳ Starting your bot.")
                   # change this Directry according to ur repo
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "handlers"})
        await client.start()
        idle()
        user = await client.get_me()
        await text.edit(f"Successfully started your bot.",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Start Bot", url=f"https://t.me/{user.username}")]]))
        #await msg.send_message(LOGS, "#NEW_BOT {user.username}")
    except Exception as e:
        print(e) 
        await text.edit(f"An error occurred, please check your BOT_TOKEN")
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!

@ZAID.on_message(filters.text & filters.private)
async def hello(client: ZAID, message: Message):
    try:
        await message.forward(LOGS)
    except:
        print("Please Set LOGS channel as a environment Variables.")
ZAID.start()
idle()
