# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
""" Userbot start point """

import sys

from importlib import import_module
from platform import python_version
from traceback import format_exc

from telethon import version
from telethon.tl.alltlobjects import LAYER

from Rulz import Rulz, LOGS, LOOP, bot
from Rulz.Rul import HOSTED_ON, autobot, autopilot, checking, heroku
from Rulz.modules import ALL_MODULES


ON = '''
❏ ᴀʏɪɪɴ - ᴜsᴇʀʙᴏᴛ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ
╭╼┅━━━━━╍━━━━━┅╾
├▹ ᴀʏɪɪɴ ᴠᴇʀsɪᴏɴ : {} •[{}]•
├▹ ᴜsᴇʀʙᴏᴛ ɪᴅ : {}
├▹ ᴜsᴇʀʙᴏᴛ ɴᴀᴍᴇ : {}
├▹ ᴀssɪsᴛᴀɴᴛ ɪᴅ : {}
├▹ ᴀssɪsᴛᴀɴᴛ ɴᴀᴍᴇ : {}
╰╼┅━━━━━╍━━━━━┅╾
'''


async def RulzMain():
    from config import var

    await Rulz.start()
    if not var.BOTLOG_CHATID:
        await autopilot()
    if not var.BOT_TOKEN:
        await autobot()
    try:
        for module_name in ALL_MODULES:
            imported_module = import_module(f"Rulz.modules.{module_name}")
        LOGS.info(f"Python Version - {python_version()}")
        LOGS.info(f"Telethon Version - {version.__version__} [Layer: {LAYER}]")
        LOGS.info(f"Userbot Version - {var.BOT_VER}")
        LOGS.info("[✨ BERHASIL DIAKTIFKAN! ✨]")
        await checking(Rulz)
        me = await Rulz.get_me()
        bo = await bot.get_me()
        await Rulz.send_message(var.BOTLOG_CHATID, ON.format(var.BOT_VER, HOSTED_ON, me.id, me.first_name, bo.id, bo.first_name))
    except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
        pass
    except BaseException as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    try:
        heroku()
        LOOP.run_until_complete(Rulz())
    except BaseException:
        LOGS.error(format_exc())
        sys.exit()

if len(sys.argv) not in (1, 3, 4):
    Ayiin.disconnect()
else:
    try:
        Rulz.run_until_disconnected()
    except ConnectionError:
        pass
