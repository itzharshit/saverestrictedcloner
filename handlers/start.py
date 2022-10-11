#Copyright By Itz-Zaid
# @Timesnotwaiting on Telegram!

from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters



@Client.on_message(filters.private & filters.command("start"))
async def start(client: Client, message: Message):
    user = await client.get_me()
    await message.reply(f"🤖 {user.first_name} is under maintenance, please wait until maintenance to be completed.\n\nParked on @TheParker_Bot")

