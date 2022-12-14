#Copyright By Itz-Zaid
# @Timesnotwaiting on Telegram!

from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters



@Client.on_message(filters.command('start') & filters.private)
async def echo(client: Client, message: Message):
    user = await client.get_me()
    await message.reply(f"**Hi {message.chat.first_name}!**\n\nI am {user.first_name}, I can save Restricted Contents of any public channel of telegram.\nJust send me link of your message i will give you that message here.")

#Requesting for file
@Client.on_message(filters.private & filters.text & filters.incoming)
async def link_handler(client: Client, message: Message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("Send only message link.",quote=True)
        return
    for link in links:
        try:
            await get_shortlink(link)
        except Exception as e:
            await message.reply(f'Error: `{e}`', quote=True)
