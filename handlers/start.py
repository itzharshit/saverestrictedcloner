#Copyright By Itz-Zaid
# @Timesnotwaiting on Telegram!
import re
import aiohttp
from pyrogram import Client
from pyrogram.types import *
from pyrogram import filters



@Client.on_message(filters.command('start') & filters.private)
async def start(client: Client, message: Message):
    user = await client.get_me()
    await message.reply(f"**Hi {message.chat.first_name}!**\n\nI am {user.first_name}, I can save Restricted Contents of any public channel of telegram.\nJust send me link of your message i will give you that message here.")

#Requesting to copy message 
@Client.on_message(filters.private & filters.text & filters.incoming)
async def link_handler(client: Client, message: Message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1 and not 't.me' in link:
        await message.reply("Send only message link.",quote=True)
        return
    for link in links:
        try:
            await copy_msg(message.chat.id), link)
        except Exception as e:
            await message.reply(f'Error: `{e}`', quote=True)


async def copy_msg(sender, msg_link):
    chat =  msg_link.split("/")[-2]
    msg_id = int(msg_link.split("/")[-1])
    if 't.me/c/' in msg_link:
        await message.reply(f'Sorry, but i can only give you message of public channel.', quote=True)
    else:
        chat =  msg_link.split("/")[-2]
        try:
            await client.copy_message(int(sender), chat, msg_id)
        except FloodWait as f:
            await message.reply(f'Bot is limited by telegram for {f.value + 2} seconds.\nPlease try again after {f.value + 2}' seconds., quote=True)
            await asyncio.sleep(f.value)
        except Exception as e: 
            return await edit.edit(f'Error: `{e}`', quote=True)
                
