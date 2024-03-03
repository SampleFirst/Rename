from pyrogram import Client, filters 
from config import ADMIN, DOWNLOAD_LOCATION
import os

dir_content = os.listdir(DOWNLOAD_LOCATION)

@Client.on_message(filters.private & filters.photo & filters.user(ADMIN))                            
async def set_thumbnail(bot, msg):       
    if not dir_content:
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        return await msg.reply("Your permanent thumbnail has been saved in the directory. \nIf you change your server or recreate the server app, you'll need to reset your thumbnail.")            
    else:    
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")               
        return await msg.reply("Your permanent thumbnail has been updated.\nIf you change your server or recreate the server app, you'll need to reset your thumbnail.")            


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMIN))                            
async def view_thumbnail(bot, msg):
    try:
        await msg.reply_photo(photo=f"{DOWNLOAD_LOCATION}/thumbnail.jpg", caption="This is your current thumbnail.")
    except FileNotFoundError:
        return await msg.reply_text("You don't have any thumbnail.")

@Client.on_message(filters.private & filters.command(["del", "del_thumb"]) & filters.user(ADMIN))                            
async def delete_thumbnail(bot, msg):
    try:
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await msg.reply_text("Your thumbnail has been removed.")
    except FileNotFoundError:
        return await msg.reply_text("You don't have any thumbnail.")
