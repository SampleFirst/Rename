from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN

@Client.on_message(filters.command("start") & filters.private)                             
async def start(bot, msg):
    txt = "This is a personal use bot 🙏." 
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Join Channel", url="https://t.me/+BKZsRSZO-wQ3ZDJl")
            ],
            [
                InlineKeyboardButton("Join Channel", url="https://t.me/+qU9Bz5jbE1I0MjFl")
            ]
        ]
    )
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview=True)
    else:
        txt = f"Hey {msg.from_user.mention}, I am a simple rename bot for personal usage.\nThis bot is made by <b><a href=https://github.com/MrMKN>MrMKN</a></b>."
        button = [
            [
                InlineKeyboardButton("Main Channel", url="https://t.me/+BKZsRSZO-wQ3ZDJl")
            ],
            [
                InlineKeyboardButton("ℹ️ Help", callback_data="help"), 
                InlineKeyboardButton("📡 About", callback_data="about")
            ] 
        ]
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)

@Client.on_callback_query(filters.regex("start"))
async def start_callback(bot, msg):
    txt = "This is a personal use bot 🙏." 
    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Join Channel", url="https://t.me/+BKZsRSZO-wQ3ZDJl")
            ],
            [
                InlineKeyboardButton("Join Channel", url="https://t.me/+qU9Bz5jbE1I0MjFl")
            ]
        ]
    )
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview=True)
    else:
        txt = f"Hey {msg.from_user.mention}, I am a simple rename bot for personal usage.\nThis bot is made by <b><a href=https://github.com/MrMKN>MrMKN</a></b>."
        button = [
            [
                InlineKeyboardButton("Main Channel", url="https://t.me/+BKZsRSZO-wQ3ZDJl")
            ],
            [
                InlineKeyboardButton("ℹ️ Help", callback_data="help"), 
                InlineKeyboardButton("📡 About", callback_data="about")
            ] 
        ]
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)

@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "Just send a file and use /rename <new name> with your file replied to.\n\n"
    txt += "Send a photo to set a thumbnail automatically.\n"
    txt += "/view to see your thumbnail.\n"
    txt += "/del to delete your thumbnail."
    button = [
        [
            InlineKeyboardButton("🚫 Close", callback_data="del"), 
            InlineKeyboardButton("⬅️ Back", callback_data="start")
        ]
    ]
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me = await bot.get_me()
    Master = "<a href=https://t.me/Mo_Tech_YT>MoTech</a> & <a href=https://t.me/venombotupdates>MhdRzn</a>"  
    Source = "<a href=https://github.com/MrMKN/Simple-Rename-Bot>Click Here</a>"
    txt = f"<b>Bot Name: {me.mention}\nMy Master's: {Master}\nSource Code: {Source}</b>"                 
    button = [
        [
            InlineKeyboardButton("🚫 Close", callback_data="del"), 
            InlineKeyboardButton("⬅️ Back", callback_data="start")
        ]
    ]
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@Client.on_callback_query(filters.regex("del"))
async def close_callback(bot, msg):
    try:
        await msg.message.delete()
    except:
        return
