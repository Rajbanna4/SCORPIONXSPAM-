from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from .. import SP1, SP2, SP3, SP4, SP5, SP6, SP7, SP8, SP9, SP10, ALIVE_PIC, OWNER_ID
from SCORPIONXSpam.plugins.help import *


SCORPION_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/33ec48ede8f590f9c40b0.jpg"

SCORPION_Button = [
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]


#USERS 


@SP1.on(events.NewMessage(pattern="/start"))
@SP2.on(events.NewMessage(pattern="/start"))
@SP3.on(events.NewMessage(pattern="/start"))
@SP4.on(events.NewMessage(pattern="/start"))
@SP5.on(events.NewMessage(pattern="/start"))
@SP6.on(events.NewMessage(pattern="/start"))
@SP7.on(events.NewMessage(pattern="/start"))
@SP8.on(events.NewMessage(pattern="/start"))
@SP9.on(events.NewMessage(pattern="/start"))
@SP10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       SCORPIONBot = await event.client.get_me()
       bot_id = SCORPIONBot.first_name
       bot_username = SCORPIOMBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheSCORPION = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [SCORPION](https://t.me/SCORPIONxSPAM)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheSCORPION,
                  SCORPION_IMG,
                  caption=ownermsg, 
                  buttons=SCORPION_Button)
       else:
            await event.client.send_file(TheSCORPION,
                  SCORPION_IMG,
                  caption=usermsg)
