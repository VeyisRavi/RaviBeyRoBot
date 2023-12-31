## Sahib HuseynH Satış Qadağandır

import logging, asyncio, random
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from AylinRobot.config import Config
from Telethon.Mesajlar import soz,  emoji, bayrag
from telethon import events, errors
import time
from telethon.tl.functions.channels import GetParticipantsRequest




logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)
 
api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []
 
ozel_list = [2074934667]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}
	
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
	
	
	
@client.on(events.NewMessage(pattern="^.tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ etmək üçün bir mesaj yazın**\n**ℹ️ Misal:** `/tag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
		
		
		
		
		
		
@client.on(events.NewMessage(pattern="^.tektag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün üserlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/tektag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 	
	
	
@client.on(events.NewMessage(pattern="^.htag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/htag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(heyvan)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(heyvan)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
	
	
@client.on(events.NewMessage(pattern="^.sehidler ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
 
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə meesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/etag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(sehidler)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(sehidler)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:**  `{rxyzdev_tagTot[event.chat_id]}`\n**🗣 Prosesi başladan:**  {rxyzdev_initT}")
 
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
@client.on(events.NewMessage(pattern="^.stag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir")
  
  admins = []
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
 
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/etag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:**  `{rxyzdev_tagTot[event.chat_id]}`\n**🗣 Prosesi başladan:**  {rxyzdev_initT}")
 
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
@client.on(events.NewMessage(pattern="^.mtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün mesaj yazın**")
  else:
    return await event.respond("**✅ Tağ edə bilməyim üçün bir mesaj yaın**\n**ℹ️ Misal:** `/mtag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
 
 
 
@client.on(events.NewMessage(pattern="^.etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/etag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
@client.on(events.NewMessage(pattern="^.rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**✅ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**✅ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın\n**ℹ️ Misal:** `/rtag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
 
@client.on(events.NewMessage(pattern="^.btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**⚠️ Bu əmr sadəcə qruplar üçün keçərlidir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz admin deyilsiz**\n**⚠️ Bu əmr sadəcə adminlər üçün keçərlidir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**❌ Köhnə mesajlar üçün userlərdən bəhs edə bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**")
  else:
    return await event.respond("**⚠️ Tağ edə bilməyim üçün bir mesaj yazın**\n**ℹ️ Misal:** `/btag Salam`")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ prosesi başladı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ prosesi tamamlandı**\n\n**📊 Tağ edilənlərin sayı:** {rxyzdev_tagTot[event.chat_id]}\n\n**👤 Prosesi başladan:** {rxyzdev_initT}")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🛑 Tağ prosesi dayandırıldı**\n\n**📊 Tağ edilənlərin sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
		


@client.on(events.NewMessage(pattern="^.admin ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "Qrup Adminlərin Siyahısı 👤\n"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n[{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation
    
    
    
    
SAHIB = Config.OWNER_ID

@client.on(events.NewMessage(pattern="^.pin ?(.*)"))
async def pin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Zəhmət olmasa bir mesaja yanıt ver ❗")
        await event.reply("Mesajı sabitlədım 📌")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} bota sahib deyilsən ❗")
 

@client.on(events.NewMessage(pattern="^.unpin ?(.*)"))
async def unpin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("Zəhmət olmasa sabitlənmiş bir mesaja yanıt ver ❗")
        await event.reply("Sabitlənmiş mesaj qaldırıldı ❗")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} bota sahib deyilsən ❗")    
        





@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))


@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        user = await event.get_user()
        username = f"[{user.first_name}](tg://user?id={user.id})"
        mesaj = (f"{username} Xoş gəldin",
                 f"{username} Gəldi 🙄",
                 f"{username} Sənin Gəlişin Məni Sevindirdi 🫠", 
                 f"{username} Aramıza Xoş Gəldin 🙋🏻",
                 f"{username} Partimizə Xoş Gəldin🥳",
                 f"{username} Bayaqdan Səni Gözləyirəm 🤩",
                 f"{username} Xoşgəldin, Pizza gətirəcəyivi düşünürdük. 🤠",
                 f"{username} Xoşgəldin, Çıxacaqsansa indidən çıx 😒.",)
        await event.reply(f"{random.choice(mesaj)}")




@client.on(events.NewMessage(pattern='@Rahid_7'))
async def handler(event):
    await event.reply(random.choice(Aylin))



Aylin = (
    "Az tağ elə sahibimi😒",
    "İşi var birazdan gələcək😇",
    "Ay bala nolub mənə de o yoxdu",
    "Az tağ elədə sahibimi",
    "Sahibim burda deyil mənə deyə bilərsən👀",
    "Evdə deyil",
    "Nolub mənə deyə bilərsən",
    "Burda deyil yəqin başqa qrupdadı😂",
    "Sahibim burda olmasada qəlbi sizinlədir😌",
    "Burda yoxdur kömək üçün mənə deyə bilərsən😇",
    "@Rahid_7 səni çağırır qaqaş👀",
    "🚷 Ban Olundun !\nSəbəb: Sahibimi tağ etdiyin üçün 🙄\n\nŞaka ya korkma 😂",
    "/ban çox tağ edirsən Sahibimi🙄",
    "/mute az tağ elə Sahibimi😑",
    "/warn birdə Sahibimi tağ eləsən ban verəcəm sənə!",
    "/fban Sahibimi çox tağ edirsiz!",
    "Sahibim dedi birazdan gələcəm👀",
    "Az tağ edin onu zəhmət olmasa🙄",
    "Onun başı qarışıqdı birazdan gələcək",
    "O daha qrupa gəlməyəcək onu mən əvəz edəcəyəm 🤖",
    "Nə istəyirsən ondan?",
    ""
)


import asyncio
import random
from telethon import events

faiz = ['10%','11%','12%','13%','14%','15%','16%','17%','18%','19%','20%','21%','22%','23%','24%','25%','26%','27%','28%','29%','30%','31%','32%','33%','34%','35%','36%','37%','38%','39%','40%','41%','42%','43%','44%','45%','46%','47%','48%','49%','50%','51%','52%','53%','54%','55%','56%','57%','58%','59%','60%','61%','62%','63%','64%','65%','66%','67%','68%','69%','70%','71%','72%','73%','74%','75%','76%','77%','78%','79%','80%','81%','82%','83%','84%','85%','86%','87%','88%','89%','90%','91%','92%','93%','94%','95%','96%','97%','98%','99%','100%']
urek = ['❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❤️‍🔥','❤️‍🩹','❣️','💕','💞','💓','💗','💖','💘','💝']


@client.on(events.NewMessage(pattern="^/eros ?(.*)|^/ship ?(.*)"))
async def eros(event):
     if event.is_private:
          return await event.respond("**ℹ️ Bu əmr qruplar üçün nəzərdə tutulub**")
     qrup = await event.get_chat() 
     istifadeciler = await client.get_participants(qrup)
     sev1, sev2 = random.sample(istifadeciler, 2)
     secirem = await event.reply(f"{random.choice(urek)} **Cütlük seçilir...**")
     await asyncio.sleep(2)
     await secirem.delete()
     await event.reply(f"{random.choice(urek)} **Cütlüklər:**\n"
                       f"[{sev1.first_name}](tg://user?id={sev1.id})" + f" 🔐 [{sev2.first_name}](tg://user?id={sev2.id})\n"
                       f"**Eşq Faizi:** {random.choice(faiz)}")





@client.on(events.NewMessage(pattern='(?i)peysər+'))
@client.on(events.NewMessage(pattern='(?i)qəhbə+'))
@client.on(events.NewMessage(pattern='(?i)cındır+'))
@client.on(events.NewMessage(pattern='(?i)peyser+'))
@client.on(events.NewMessage(pattern='(?i)qehbe+'))
@client.on(events.NewMessage(pattern='(?i)suka+'))
@client.on(events.NewMessage(pattern='(?i)küçük+'))
@client.on(events.NewMessage(pattern='(?i)blet+'))
@client.on(events.NewMessage(pattern='(?i)blət+'))
@client.on(events.NewMessage(pattern='(?i)dalbayok+'))
@client.on(events.NewMessage(pattern='(?i)pidr+'))
@client.on(events.NewMessage(pattern='(?i)xnxx+'))
@client.on(events.NewMessage(pattern='(?i)porno+'))
@client.on(events.NewMessage(pattern='(?i)sirtiq+'))
@client.on(events.NewMessage(pattern='(?i)sırtıq+'))
@client.on(events.NewMessage(pattern='(?i)kucuy+'))
@client.on(events.NewMessage(pattern='(?i)küçüy+'))
@client.on(events.NewMessage(pattern='(?i)gic+'))
@client.on(events.NewMessage(pattern='(?i)sik+'))
@client.on(events.NewMessage(pattern='(?i)dalyok+'))
@client.on(events.NewMessage(pattern='(?i)oruspo+'))
@client.on(events.NewMessage(pattern='(?i)qehbə+'))
@client.on(events.NewMessage(pattern='(?i)qəhbe+'))
@client.on(events.NewMessage(pattern='(?i)amcıq+'))
@client.on(events.NewMessage(pattern='(?i)amcığ+'))
@client.on(events.NewMessage(pattern='(?i)amk+'))
@client.on(events.NewMessage(pattern='(?i)bled+'))
@client.on(events.NewMessage(pattern='(?i)bləd+'))
@client.on(events.NewMessage(pattern='(?i)cindir+'))
@client.on(events.NewMessage(pattern='(?i)ostur+'))
@client.on(events.NewMessage(pattern='(?i)dumsuy+'))
@client.on(events.NewMessage(pattern='(?i)dumsuk+'))
@client.on(events.NewMessage(pattern='(?i)slk+'))
@client.on(events.NewMessage(pattern='(?i)pox+'))
@client.on(events.NewMessage(pattern='(?i)qehbbeninnn+'))
@client.on(events.NewMessage(pattern='(?i)qehebe+'))
@client.on(events.NewMessage(pattern='(?i)qehbbeeeeee'))
@client.on(events.NewMessage(pattern='(?i)qehbbbeeee+'))
@client.on(events.NewMessage(pattern='(?i)gəhbə+'))
@client.on(events.NewMessage(pattern='(?i)qot+'))
@client.on(events.NewMessage(pattern='(?i)amcıg+'))
@client.on(events.NewMessage(pattern='(?i)gehbe+'))
@client.on(events.NewMessage(pattern='(?i)siik+'))
@client.on(events.NewMessage(pattern='(?i)gij+'))
@client.on(events.NewMessage(pattern='(?i)sg+'))
@client.on(events.NewMessage(pattern='(?i)qəhi+'))
@client.on(events.NewMessage(pattern='(?i)qehi+'))
@client.on(events.NewMessage(pattern='(?i)meki+'))
@client.on(events.NewMessage(pattern='(?i)məki+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.delete()      
    await event.reply(f"🔞 Söyüş yazdığına görə mesajı sildim.") 

@client.on(events.NewMessage(incoming=True, pattern="^[!/]purge$"))
async def purge_messages(event):
    start = time.perf_counter()
    if event.is_private:
        await event.respond("Bu əmri yalnız qruplarda icra edə bilərsiniz.", parse_mode='markdown')
        return

    if not await is_group_admin(event):
        await event.respond("Bu əmri yalnız qrup yönəticiləri icra edə bilər.", parse_mode='markdown')
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.respond("Silməyə başlayacağım mesaja yanıt ver.")
        return

    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"🗑️ Təmizləmə prosesi {time_:0.2f} saniyədə tamamlandı"
    await event.respond(text, parse_mode='markdown')


async def is_group_admin(event):
    """
    Checks if the user is a group admin
    """
    try:
        user = await event.client.get_entity(event.input_chat)
        user_info = await event.client.get_participants(user, filter=ChannelParticipantsAdmins, limit=100)
        for u in user_info:
            if u.id == event.sender_id:
                return True
    except errors.rpcerrorlist.ChatAdminRequiredError:
        pass
    return False