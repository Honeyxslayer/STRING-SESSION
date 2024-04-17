from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention}🦋,

Tʜɪs ɪs {me2},
Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.
ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ sʜᴀʀᴇ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴛᴏ ᴀɴʏᴏɴᴇ 🤝.

Mᴀᴅᴇ ᴡɪᴛʜ ❤ ʙʏ : [ʜᴏɴᴇʏ](https://t.me/OgHoneyy) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Honey_networks"),
                    InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/OgHoneyy")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
