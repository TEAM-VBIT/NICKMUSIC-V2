```python
import asyncio
import os
import shutil
import socket
from datetime import datetime

import urllib3
from pyrogram import filters

import config
from VampuMusic import app
from VampuMusic.misc import HAPP, SUDOERS, XCB
from VampuMusic.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from VampuMusic.utils.decorators.language import language
from VampuMusic.utils.pastebin import VampuBin

# Git Optional Fix
try:
    from git import Repo
    from git.exc import GitCommandError, InvalidGitRepositoryError

    GIT_AVAILABLE = True
except Exception:
    Repo = None
    GitCommandError = Exception
    InvalidGitRepositoryError = Exception
    GIT_AVAILABLE = False

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


@app.on_message(
    filters.command(
        ["getlog", "logs", "getlogs"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & SUDOERS
)
@language
async def log_(client, message, _):
    try:
        await message.reply_document(document="log.txt")
    except Exception:
        await message.reply_text(_["server_1"])


@app.on_message(
    filters.command(
        ["update", "gitpull"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & SUDOERS
)
@language
async def update_(client, message, _):

    if not GIT_AVAILABLE:
        return await message.reply_text(
            "Git updater disabled on this deployment."
        )

    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["server_2"])

    response = await message.reply_text(_["server_3"])

    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit(_["server_4"])
    except InvalidGitRepositoryError:
        return await response.edit(_["server_5"])
    except Exception:
        return await response.edit(
            "Git repository unavailable."
        )

    try:
        os.system(
            f"git fetch origin {config.UPSTREAM_BRANCH} > /dev/null 2>&1"
        )

        await asyncio.sleep(5)

        verification = ""

        for checks in repo.iter_commits(
            f"HEAD..origin/{config.UPSTREAM_BRANCH}"
        ):
            verification = str(checks.count())

        if verification == "":
            return await response.edit(_["server_6"])

        await response.edit(
            "Update available. Restarting..."
        )

        os.system("git stash > /dev/null 2>&1")
        os.system("git pull > /dev/null 2>&1")

    except Exception as e:
        return await response.edit(
            f"Update failed:\n{e}"
        )

    if await is_heroku():
        try:
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception:
            return
    else:
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && bash start")
        exit()


@app.on_message(filters.command(["restart"]) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("Restarting...")

    ac_chats = await get_active_chats()

    for x in ac_chats:
        try:
            await app.send_message(
                chat_id=int(x),
                text=f"{app.mention} is restarting..."
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except Exception:
            pass

    try:
        shutil.rmtree("downloads")
    except Exception:
        pass

    try:
        shutil.rmtree("raw_files")
    except Exception:
        pass

    try:
        shutil.rmtree("cache")
    except Exception:
        pass

    await response.edit_text(
        "Restart process started..."
    )

    os.system(f"kill -9 {os.getpid()} && bash start")
```
