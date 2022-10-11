#Copyright By Itz-Zaid
# @Timesnotwaiting on Telegram!

from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters



@Client.on_message(filters.private & filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply("This bot is under maintenance, please wait till untill maintenance to be completed.\n\nParked on @TheParker_Bot")

