from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 
import config

class BUTTONS(object):
    ABUTTON = [
    [
        InlineKeyboardButton("sυᴘᴘᴏʀᴛ", url="https://t.me/llNICK_UPDATESll"),
        InlineKeyboardButton("υᴘᴅᴧᴛᴇs", url="https://t.me/llNICK_UPDATESll")
    ],
    [
        InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=config.OWNER_ID),
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settingsback_helper")
    ]
]

    INFO_BUTTON = [
    [
        InlineKeyboardButton("ʀєᴘσ", callback_data="gib_source"),
        InlineKeyboardButton("ʏᴛ-ᴀᴘɪ", callback_data="bot_info_data"),
        InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ", callback_data="LG"),
    ],
    [
        
        InlineKeyboardButton("ᴘʀɪᴠᴧᴄʏ", url="https://i.ibb.co/VYD85Df0/x.jpg"),
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settingsback_helper"),
    ]
    ]
    


    INFO_NEW = [
    [
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settings_back_helper")],
    ]
    
    
