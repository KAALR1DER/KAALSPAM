from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "Uploaded to https://telegra.ph/file/20dda006e65de620ee475.jpg in 1 seconds."
  

          
rizoel = "✧ 𝐊𝐀𝐀𝐋 𝑆𝑃𝐴𝑀 𝐼𝑍𝑍 𝐴𝐿𝐼𝑉𝐸𝐸 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **𝐊𝐀𝐀𝐋𝐒𝐏𝐀𝐌 ᴠᴇʀsɪᴏɴ**  : `{kaalversion}`\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/KAAL_NETWORK"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/HEAVEN_ARMY")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/KAALR1DER/KAALSPAM")
        ]
        ]
        )
    
