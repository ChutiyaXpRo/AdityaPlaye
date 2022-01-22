import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ffa00735d1202e76d3b05.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
⚡ ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᏟᎡᎬᎪͲϴᎡ : [ᏃᎬᏢᎻᎽᎡ](https://t.me/Zephyr_Owner)
┣★ ႮᏢᎠᎪͲᎬՏ : [ᏃᎬᏢᎻᎽᎡ ✘ ՏᎬᎡᏙᎬᎡ](https://t.me/adityaserver)
┣★ ՏႮᏢᏢϴᎡͲ : [ҒᏆΝᎪᏞ ՏͲᎡᏆᏦᎬ](https://t.me/FinalStrikeOp)
┣★ ՏϴႮᎡᏟᎬ › : [ՏϴϴΝ](https://t.me/ZephyrSoon)
┗━━━━━━━━━━━━━━━━━┛

💫 ᏆҒ ᎽϴႮ ᎠϴΝͲ ᏦΝϴᏔ ᎻϴᏔ Ͳϴ ႮՏᎬ ᏴϴͲ , ᏢᏞᎬᎪՏᎬ ՏᎷ ϴΝ  [ᏃᎬᏢᎻᎽᎡ](https://t.me/Zephyr_Owner) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᎫϴᏆΝ ҒϴᎡ ᎷϴᎡᎬ ᏴϴͲՏ ❱ ➕", url=f"https://t.me/ZephyrProjects")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/c6e1041c6c9a12913f57a.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/FinalStrikeOp")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ffa00735d1202e76d3b05.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 💞", url=f"https://t.me/Zephyr_Owner")
                ]
            ]
        ),
    )
