import time

from telethon import version
from UltronBot import ALIVE_NAME, StartTime, version
from UltronBot.utils import admin_cmd, edit_or_reply, sudo_cmd
from UltronBot.cmdhelp import CmdHelp
from . import *
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "UltronBot"
 PIC = "https://telegra.ph/file/d69901c925579aaf67ab9.jpg"
CUSTOM_ALIVE_TEXT =  "ℓєgєи∂ Choice Ultronϐοτ"
CUSTOM_YOUR_GROUP =  "@UltronBot_xD"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def amireallyalive(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)

    if  PIC:
         ULTRON_caption = f"**{mention}**\n"
        
         ULTRON_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
         ULTRON_caption += f"     💫 ✞︎t͛ẞ̸ Ultronẞø✞︎ ιѕ αωακє 💫\n"
         ULTRON_caption += f"•🔥•UltronBot-Mix    : ν3.0\n"
         ULTRON_caption += f"•🔥•𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽      : `{version.__version__}`\n"
         ULTRON_caption += f"•🔥•`SATYABOT` :  V.1 \n"
         ULTRON_caption += f"•🔥•`OS:`       : Kali GNU/Linux Rolling x86_64 \n"                                        
         ULTRON_caption += f"•🔥•𝚄𝙿𝚃𝙸𝙼𝙴         : `{uptime}`\n"
         ULTRON_caption += f"•🔥•𝙲𝙷𝙰𝙽𝙽𝙴𝙻        : [𝕮нαииєℓ](t.me/UltronBot_OP)\n"
         ULTRON_caption += f"•🔥•𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 : [Group](t.me/UltronBot_xD\n"   

        await event.client.send_file(
            event.chat_id,  PIC, caption= ULTRON_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"______ ULTRON-𝐔𝐬𝐞𝐫𝐛𝐨𝐭______\n"
            f"╔════❰🐍 Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ🐍 ❱═❍⊱❁۪۪¤๋͜\n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼Developer^By┣⪼ [Legend-Lx](t.me/Legendl_Mr_Hacker) \n"
            f"║┣⪼Edition^Developer^By ┣⪼ [Legend-Os](t.me/The_LegendBoy) \n"
            f"║┣⪼Ⲟⲱⲛⲉʀ      ┣⪼ [ℓєgєи∂-ℓx](t.me/Legendl_Mr_Hacker) \n"
            f"║┣⪼Ⲋⲧⲁⲧυⲋ      ┣⪼ Ⲟⲛⳑⲓⲛⲉ\n"
            f"║┣⪼Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ ┣⪼ {mention}\n"
            f"║┣⪼Ⳙⲣⲧⲓⲙⲉ      ┣⪼  {uptime}\n"
            f"║┣⪼Ⲃⲟⲧ Ⲣⲓⲛⳋ     ┣⪼  {uptime}\n"   
            f"║┣⪼Ⲣⲩⲧⲏⲟⲛ       ┣⪼  {PYTHONversion}\n"
            f"║┣⪼`Os:`        ┣⪼   Kali GNU/Linux Rolling x86_64 \n"                                       
            f"║┣⪼Ⲧⲉⳑⲉⲧⲏⲟⲛ     ┣⪼  {version.__version__} \n"
            f"║┣⪼[✨🐍PYTHON┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/Python_Userbot_Support)\n"
            f"║╰━━━━━━━━━━━━━━━➣ \n"
            f"╚══════════════════❍⊱❁۪۪¤๋͜-  \n"
        )

CmdHelp("awake").add_command(
    'bot', None, 'υѕє αи∂ ѕєє'
).add()
