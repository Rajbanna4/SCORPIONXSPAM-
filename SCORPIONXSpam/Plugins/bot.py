import os
import sys
import heroku3
from SCORPIONXSpam import SCORPIONVersion, SP1, SP2, SP3, SP4, SP5 , SL6, SP7, SP8, SP9, SP10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, SCORPIONVersion
from SCORPIONXSpam import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from SCORPIONXSpam import ALIVE_PIC
from telethon import events, version, Button
from datetime import datetime
from telethon.tl import functions

from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)

SCORPION_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/33ec48ede8f590f9c40b0.jpg"
  

scorpion = "✯ SCORPIOM 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲 ✯\n\n"
scorpion += f"═══════════════════\n"
scorpion += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"
scorpion += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
scorpion += f"• **scorpionXsᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{SCORPIONVersion}`\n"
scorpiom += f"═══════════════════\n\n"   

                                  
@SP1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  SCORPION_PIC,
                                  caption=scropion,
                                  buttons=[
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/ERR0rMK/PythonBot13")
        ]
        ]
        )
    
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

@SP1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping1(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Ping..."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f" 
   SCORPION X     
       \n`{ms}` ms\n⚔️🔥𝗦𝗣𝗔𝗠🔥⚔️")


@SP1.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%sping2(?: |$)(.*)" % hl))
async def ping2(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Ping..."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🔥🥳𝐒𝐏𝐄𝐄𝐃🔥🥳!\n`{ms}` 𝗺𝘀\n🤩🥀—𝙁・𝙐𝘾𝙆 𓆩𝙊𝙁𝙁 🤫😂𓆪🥀 𝐒𝐏𝐀𝐌𝐁𝐎𝐓🤩")


@SP1.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%sping3(?: |$)(.*)" % hl))
async def ping3(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Ping..."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🍷🔥SCORPION🔥🍷.!\n`{ms}` ms\n⚔️ 𓆩SPAM𓆪 ⚔️")
        
        

@SP1.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "Restarting Your SCORPION X Spam...\nPlease Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await SP1.disconnect()
        except Exception:
            pass
        try:
            await SP2.disconnect()
        except Exception:
            pass
        try:
            await SP3.disconnect()
        except Exception:
            pass
        try:
            await SP4.disconnect()
        except Exception:
            pass
        try:
            await SP5.disconnect()
        except Exception:
            pass
        try:
            await SP6.disconnect()
        except Exception:
            pass
        try:
            await SP7.disconnect()
        except Exception:
            pass
        try:
            await SP8.disconnect()
        except Exception:
            pass
        try:
            await SP9.disconnect()
        except Exception:
            pass
        try:
            await SP10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@SP1.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a SUDO...")
        scorpiom = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user.\n**Restarting**...\nPlease wait a minute...")
        heroku_var[scorpion] = newsudo


@SP1.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
async def rmsudo(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Removing user from SUDO...")
        scorpion = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = " ".join(sudousers.split(" ").remove(target))
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Removed `{target}` ** from sudo users.\n**Restarting**...\nPlease wait a minute...")
        heroku_var[mk] = newsudo


@SP1.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SUDO_USERS:
        mk_j = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = scorpion_j[0]
            text = "𝐆𝐀𝐀𝐍𝐃 𝐌𝐈𝐋 𝐆𝐘𝐀𝐀 𝐁𝐇𝐀𝐈𝐈 💋💦"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝐂𝐇𝐀𝐋𝐈𝐘𝐄 𝐆𝐀𝐍𝐃 𝐌𝐀𝐑𝐍𝐀 𝐒𝐇𝐔𝐑𝐔 𝐊𝐀𝐑𝐓𝐄 𝐇𝐀𝐈 🍑💋💦")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@SP1.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
async def get_users(event):
    if event.sender_id in SUDO_USERS:
        rkp = await event.reply("`Processing...`")
    else:
        rkp = await event.edit("`Processing...`")
    rk1 = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await rkp.edit("`Sorry, Can add users here`")
    s = 0
    f = 0
    error = "None"

    await rkp.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(rk1.full_chat.id):
        try:
            if error.startswith("Too"):
                return await rkp.edit(
                    f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await rkp.edit(
                f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await rkp.edit(
        f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
    )

     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`ʟᴏʟ ɴᴏᴛ ᴛʜɪs ɢʀᴘ`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info
