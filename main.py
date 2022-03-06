import os
import random
import re

from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(':memory:', os.getenv('API_ID'), os.getenv('API_HASH'), bot_token=os.getenv('BOT_TOKEN'))

PATTERN_UA = re.compile('Слава Україні.?$', re.I)
PATTERN_BE = re.compile('Слава Украіне.?$', re.I)
PATTERN_EN = re.compile('Glory to Ukraine.?$', re.I)


@app.on_message(filters.private)
async def on_private(_: Client, message: Message):
    await message.delete()


@app.on_message((filters.regex(PATTERN_UA) | filters.regex(PATTERN_BE)) & ~filters.edited)
async def on_glory_ua_and_be(_: Client, message: Message):
    await message.reply('Героям слава!')


@app.on_message(filters.regex(PATTERN_EN) & ~filters.edited)
async def on_glory_en(_: Client, message: Message):
    await message.reply('Glory to the heroes!')


@app.on_message(~filters.edited)
async def on_any(_: Client, message: Message):
    if random.randint(1, 100) == 100:
        await message.reply('Слава Україні!')


if __name__ == '__main__':
    app.run()
