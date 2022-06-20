from SORPIONXSpam import SP1, SP2, SP3, SP4, SP5, SP6, SP7, SP8, SP9, SP10, SUDO_USERS
from telethon import events, Button
from SCORPIONXSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/33ec48ede8f590f9c40b0.jpg"

SCORPION_Help = "__Click On Below Buttons for help__"


@SP1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SP2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SP3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SP4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SP5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SP6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SP7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SP8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SP9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@SP10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=SCORPION_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: Userbot Cmds
command:
i) {hl}ping
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : Owner Cmd

**Echo**: To Active Echo On Any User
command:
i) {hl}addecho <reply to user>
ii) {hl}rmecho <reply to user>

**Leave**: To Leave Group/channel
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group

**Packspam**: Sticker Pack Spam
i) {hl}packspam (replying to any sticker)

**© @SCORPIONxARMY1**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**Raid:** Activates raid on any individual user for given range.
command:
i) {hl}raid <count> <username>
ii) {hl}raid <count> <reply to user>

**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**Replyraid:** Activates Reply Raid on the user!!
command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**Dreplyraid:** Deactivates reply raid on the user!!
command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @SCORPIONxARMY1**
"""

spam_msg = f"""
**Help Spam Cmds**

**Spam**: Spams a message for given counter(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**Bigspam**: Spams a message for given counter.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**Delayspam**: Delay spam a text for given counter after given time.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**Pornspam**: Pornography Spam.
command:
i) {hl}pornspam <count>

**Hang**: Spams hanging message for given counter.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @SCORPIONxARMY1**
"""                     
           
           
@SP1.on(events.CallbackQuery(pattern=r"help_back"))
@SP2.on(events.CallbackQuery(pattern=r"help_back"))
@SP3.on(events.CallbackQuery(pattern=r"help_back"))
@SP4.on(events.CallbackQuery(pattern=r"help_back"))
@SP5.on(events.CallbackQuery(pattern=r"help_back"))
@SP6.on(events.CallbackQuery(pattern=r"help_back"))
@SP7.on(events.CallbackQuery(pattern=r"help_back"))
@SP8.on(events.CallbackQuery(pattern=r"help_back"))
@SP9.on(events.CallbackQuery(pattern=r"help_back"))
@SP10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            SCORPION_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra cmds", data="extra"),
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own 🔥 SCORPUON 𝗫 𝗦𝗣𝗔𝗠 🔥 Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@SP1.on(events.CallbackQuery(pattern=r"spam"))
@SP2.on(events.CallbackQuery(pattern=r"spam"))
@SP3.on(events.CallbackQuery(pattern=r"spam"))
@SP4.on(events.CallbackQuery(pattern=r"spam"))
@SP5.on(events.CallbackQuery(pattern=r"spam"))
@SP6.on(events.CallbackQuery(pattern=r"spam"))
@SP7.on(events.CallbackQuery(pattern=r"spam"))
@SP8.on(events.CallbackQuery(pattern=r"spam"))
@SP9.on(events.CallbackQuery(pattern=r"spam"))
@SP10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own 🔥 𓆩SCORPION𓆪 𝗫 𝗦𝗣𝗔𝗠 🔥 Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@SP1.on(events.CallbackQuery(pattern=r"raid"))
@SP2.on(events.CallbackQuery(pattern=r"raid"))
@SP3.on(events.CallbackQuery(pattern=r"raid"))
@SP4.on(events.CallbackQuery(pattern=r"raid"))
@SP5.on(events.CallbackQuery(pattern=r"raid"))
@SP6.on(events.CallbackQuery(pattern=r"raid"))
@SP7.on(events.CallbackQuery(pattern=r"raid"))
@SP8.on(events.CallbackQuery(pattern=r"raid"))
@SP9.on(events.CallbackQuery(pattern=r"raid"))
@SP10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own 🔥 𓆩SCORPION𓆪 𝗫 𝗦𝗣𝗔𝗠 🔥 Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@SP1.on(events.CallbackQuery(pattern=r"extra"))
@SP2.on(events.CallbackQuery(pattern=r"extra"))
@SP3.on(events.CallbackQuery(pattern=r"extra"))
@SP4.on(events.CallbackQuery(pattern=r"extra"))
@SP5.on(events.CallbackQuery(pattern=r"extra"))
@SP6.on(events.CallbackQuery(pattern=r"extra"))
@SP7.on(events.CallbackQuery(pattern=r"extra"))
@SP8.on(events.CallbackQuery(pattern=r"extra"))
@SP9.on(events.CallbackQuery(pattern=r"extra"))
@SP10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own 🔥 𓆩SCORPION𓆪 𝗫 𝗦𝗣𝗔𝗠 🔥 Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
