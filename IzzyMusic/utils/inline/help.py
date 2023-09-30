from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from IzzyMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🍷 𝐀𖽴𖾕𖽹𖽡 😻",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🍷 𝐀𖽪𖾓𖽻 😻",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="🍷 𝐁𖾘𖽙𖽝ᴋ 𝀚 𝐋𖽹𖾗𖾓😻",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🍷 𝐁𖽷𖽙𖽖𖽴𖽝𖽖𖾗𖾓 😻",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="🍷 𝐆𖽜𖽖𖽡 😻",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🍷 𝐋ʏ𖽷𖽹𖽝𖾗 😻",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🍷 𝐏𖽹𖽡ꮐ 😻",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="🍷 𝐏𖾘𖽖ʏ 😻",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="🍷 𝐏𖾘𖽖ʏ 𝀚 𝐋𖽹𖾗𖾓 😻",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🍷 𝐕𖽹𖽴𖽞𖽙 𝀚 𝐂𖽻𖽖𖾓 😻",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="🍷 𝐒𖾓𖽖𖾖𖾓 😻",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="🍷 𝐒𖽪𖽴𖽙 😻",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🍷 𝐇𖽞𖾘𖽳 😻",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
