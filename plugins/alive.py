import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7336a7da0b4ae78fd63cc.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🐯 Hҽʅʅσ, I αɱ Sυρҽɾϝαʂƚ Hιɠԋ Qυαʅιƚყ 
Nσ Lαɠ Vƈ Mυʂιƈ Pʅαყҽɾ Bσƚ.

┏━━━━━━━━━━━━━━━━━┓
┣★ Cɾҽαƚσɾ 🛠️  [𝚂𝚞𝚗𝚗𝚢 𝙼𝚎𝚎𝚗𝚊](https://t.me/Sunny_meena)
┣★ Cɾҽαƚσɾ 🛠️ [𝙳𝚎𝚎𝚙𝚊𝚗𝚜𝚑𝚞 𝙼𝚎𝚎𝚗𝚊](https://t.me/STD_DEEPANSHU)
┣★ Uρԃαƚҽʂ 📢 [STD Bɾαɳԃ](https://t.me/STD_UPDATE)
┣★ Sυρρσɾƚ ☣️ [STD Cԋαƚ](https://t.me/STD_FRIENDS_FOREVER)
┣★ Cԋαƚƚιɳɠ ©️ [STD Cԋαƚ](https://t.me/best_friends_chat_group)
┗━━━━━━━━━━━━━━━━━┛

🗽 Jυʂƚ Aԃԃ Mҽ » Tσ Yσυɾ Gɾσυρ Aɳԃ
Eɳʝσყ Bҽʂƚ Qυαʅιƚყ ❥︎ Mυʂιƈ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Aԃԃ Mҽ Tσ Yσυɾ Gɾσυρ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", f"/start@{BOT_USERNAME}", "/alive", "/BGT",  ".Kaal"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7336a7da0b4ae78fd63cc.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛪ Jσιɳ Oυɾ Cԋαƚ Gɾσυρ  🗽", url=f"https://t.me/BGT_CHAT")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "Deepanshu", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7336a7da0b4ae78fd63cc.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛪ Cʅιƈƙ Mҽ Tσ Gҽƚ Rҽρσ 🗽", url=f"https://t.me/STD_DEEPANSHU")
                ]
            ]
        ),
    )
