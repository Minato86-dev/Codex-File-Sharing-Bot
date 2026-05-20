#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text =f"<b>Mera Nirmaan Humari Anime Website TpXSub.com Ki Files Store Karne Ke Liye Kiya Gaya Hai, Mere <a href='tg://user?id={OWNER_ID}'>Nirmaata</a> hain.\n\nHumare Saath Bane Rehne Ke Liye Humare News Channel: @TeamProjectXNews Ko Join Karein, Aur Saath Hi Humare Group: @TpXNew Ko Bhi Join Karein!</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
