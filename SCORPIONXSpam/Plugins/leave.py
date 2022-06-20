from SCORPIONXSpam import SP1, SP2, SP3, SP4, SP5, SP6, SP7, SP8, SP9, SP10, SUDO_USERS
from SCORPIONXSpam import CMD_HNDLR as hl
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events

@SP1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        SCORPION_leave = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = SCORPION_leave[0]
            Xd = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(Xd))
                await event.edit("Succesfully Left ✅")
            except Exception as e:
                await event.edit(str(e))
         
        else:
             bc = e.chat_id
             Xd = int(bc)
             text = "I'm Leaving This Group....."
             if e.is_private:
                  dik = f"You Can't Do this Here !! \n\n {hl}leave <Channel or Chat ID> \n {hl}leave : type in the group bot will auto leave that group !"
                  await e.reply(dik, parse_mode=None, link_preview=None )
             else:
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  try:
                      await event.client(LeaveChannelRequest(Xd))
                  except Exception as e:
                      await event.edit(str(e))
