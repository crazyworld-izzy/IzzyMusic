


from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🦋𝆺𝅥𓆩〭〬𝐂𖽪֟፝𖾓𖾝 ԍ𖽹𖾜֟፝𖾘 𝆺𝅥 𝐒𖽪𖽳𖽳𖽙𖽷𖾓😻⤍🖤",
                url="https://t.me/cute_girl_support",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
