from config import INDEX_USERNAME, SCHEDULE_ID, STATUS_ID, UPLOADS_USERNAME
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button1 = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="View Schedule", url= f"https://t.me/{UPLOADS_USERNAME}/{SCHEDULE_ID}")
            ],
            [
                InlineKeyboardButton(text="Index Channel", url= f"https://t.me/{INDEX_USERNAME}"),
                InlineKeyboardButton(text="Support", url= f"https://t.me/thoursbridi")
            ]
        ]
    )

button2 = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Check Queue", url= f"https://t.me/{UPLOADS_USERNAME}/{STATUS_ID}")
            ]
        ]
    )
