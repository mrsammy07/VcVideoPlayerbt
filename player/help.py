"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  SammyXD <https://github.com/TeamDeeCode>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import asyncio
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified

CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME
MENU_TEXT = "🥳 **Hi [{}](tg://user?id={})**,\n\nI'm **Vc Video Player**. \nLet's Enjoy Cinematic View  of Group Video Player With Your Friend. Developed By Developers of 💞 @TeamDeeCode!"
DEVS_TEXT = """
🔥 --**CREDIT FOR INNEXIA DEVS**-- :

\u2022 Here Some Developers Helping in Making The Vc Video Player.
"""
HELP_TEXT = """
🍂 --**Setting Up**-- :

\u2022 Start a voice chat in your channel or group.
\u2022 Add bot and user account in chat with admin rights.
\u2022 Then use /stream commands as a reply to an video file.

🍂 --**Common Commands**-- :

\u2022 `/start` - start the bot
\u2022 `/help` - show this help message
\u2022 `/stream` - reply to a any video!
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
        InlineKeyboardButton(
            text="Back", callback_data="menu"),
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="menu":
        buttons = [
            [
                InlineKeyboardButton('Help', callback_data="help"),
                InlineKeyboardButton('Devs', callback_data="devs")
                ],[
                InlineKeyboardButton('Support', url='https://t.me/DeeCodeSupport'),
                InlineKeyboardButton('Channel', url='https://t.me/DeeCodeBots')
                ],[
                InlineKeyboardButton('Summon Me', url='http://t.me/SiderzStreamBot?startgroup=true"),
        ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                MENU_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start", f"start@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton('Help', callback_data="help"),
                InlineKeyboardButton('Devs', callback_data="devs")
                ],[
                InlineKeyboardButton('Support', url='https://t.me/DeeCodeSupport'),
                InlineKeyboardButton('Channel', url='https://t.me/DeeCodeBots')
                ],[
                InlineKeyboardButton('Summon Me', url='http://t.me/SiderzStreamBot?startgroup=true"),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=MENU_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help", f"help@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def help(client, message):
    buttons = [
            [
        InlineKeyboardButton(
            text="Back", callback_data="menu"),
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HELP_TEXT, reply_markup=reply_markup)
