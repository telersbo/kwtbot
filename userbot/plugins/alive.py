# For @TeleBotHelp
"""Check if your userbot is working."""
import os
import requests
import time
from PIL import Image
from io import BytesIO
from userbot import ALIVE_NAME, telever
from userbot.utils import admin_cmd, sudo_cmd
from userbot.__init__ import StartTime
from datetime import datetime
from userbot.uniborgConfig import Config

ALV_PIC = os.environ.get("ALIVE_PIC" , None)

if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
    
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

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@TeleBotSupport"

@telebot.on(admin_cmd(outgoing=True, pattern="alive"))
@telebot.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        tele = f"**Welcome To TeleBot **\n\n"
        tele += "`مهلا! أنا حي. جميع الأنظمة متصلة بالإنترنت وتعمل بشكل طبيعي!`\n\n"
        tele += f"**✧ Telethon version :** `{version.__version__}\n`"
        tele += f"**✧ Kwtbot Version :** `{catversion}`\n"
        tele += f"**✧ More Info :** {@kwtbot}\n"
        tele += f"**✧ Uptime :** `{uptime}\n`"
        tele += f"**✧ Database Status :** `All OK 👌!\n`"
        tele += f"**✧ My Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
        tele += "   ✧ [ GitHub ](https://github.com/TH7RM/kwtbot)"

        chat = await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC,caption=tele, link_preview = False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/16a24c2f4d4b5435bf7b4.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(alive.chat_id, f"**Welcome To TeleBot **\n\n"
                "`مهلا! أنا حي. جميع الأنظمة متصلة بالإنترنت وتعمل بشكل طبيعي!`\n\n"
                "**✧ Telethon version :** `{version.__version__}\n`"
                f"**✧ Kwtbot Version :** `{catversion}`\n"
                "**✧ More Info :** {@kwtbot}\n"
                f"**✧ Uptime :** `{uptime}\n`"
                "**✧ Database Status :** `All OK 👌!\n`"
                f"**✧ My Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
                "   ✧ [ GitHub ](https://github.com/TH7RM/kwtbot)", link_preview = False)
        await borg.send_file(alive.chat_id, file=sticker) 
        await alive.delete()
