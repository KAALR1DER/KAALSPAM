from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/20dda006e65de620ee475.jpg in 1 seconds."
  

          
rizoel = "β§ ππππ πππ΄π πΌππ π΄πΏπΌππΈπΈ β§\n\n"

rizoel += f"ββββββββββββββββββββ\n"

rizoel += f"β£β£ **α΄Κα΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `3.9.6`\n"

rizoel += f"β£β£ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `{version.__version__}`\n"

rizoel += f"β£β£ **ππππππππ α΄ α΄ΚsΙͺα΄Ι΄**  : `{kaalversion}`\n"

rizoel += f"ββββββββββββββββββββ\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("α΄Κα΄Ι΄Ι΄α΄Κ", "https://t.me/KAAL_NETWORK"),
        Button.url("sα΄α΄α΄α΄Κα΄", "https://t.me/HEAVEN_ARMY")
        ],
        [
        Button.url("β’ Κα΄α΄α΄ β’", "https://github.com/KAALR1DER/KAALSPAM")
        ]
        ]
        )
    
