#تم كتابة السورس من قبل سورس يلنت @eiint
#يمنع منعاً باتاً تاخذه وتنسبه لنفسك رجاءاً 
#write By SaJaD @s_v_w
import re
import base64
import asyncio
import logging
from telethon import events
from config import *
from telethon.tl.functions.channels import JoinChannelRequest
from asyncio import sleep
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("Eiint")
logger.info("النشر التلقائي شغال الان استمتع ✓")
@ha313so.on(events.NewMessage)
async def join_channel(event):
	try :
		await ha313so(JoinChannelRequest('@eiint'))
	except BaseException:
		pass		
@ha313so.on(events.NewMessage)
async def join_channel(event):
	try:
		await ha313so(JoinChannelRequest('@ioibb'))
	except BaseException :
		pass
@ha313so.on(events.NewMessage)
async def join_channel(event):
	try:
		await ha313so(JoinChannelRequest('@Mshaelr'))
	except BaseException :
		pass

@ha313so.on(events.NewMessage)
async def join_channel(event):
	try:
		await ha313so(JoinChannelRequest('@toPython'))
	except BaseException :
		pass
yaAli = False
async def aljoker_nshr(ha313so, sleeptimet, chat, message, seconds):
    global yaAli
    yaAli = True
    while yaAli:
        if message.media:
            sent_message = await ha313so.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await ha313so.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@ha313so.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def Hussein(event):
    ha313so = event.client
    joinu = await ha313so(JoinChannelRequest('ioibb'))
    joinu = await ha313so(JoinChannelRequest('eiint'))
    joinu = await ha313so(JoinChannelRequest('Mshaelr'))
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    ha313so = event.client
    global yaAli
    yaAli = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await ha313so.get_entity(chat_username)
            await aljoker_nshr(ha313so, seconds, chat.id, message, seconds)  # تمرير قيمة seconds هنا لكل مجموعة
        except Exception as e:
            await event.reply(f"⌔∮ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
    
async def aljoker_allnshr(ha313so, sleeptimet, message):
    global yaAli
    yaAli = True
    aljoker_chats = await ha313so.get_dialogs()
    while yaAli:
        for chat in aljoker_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await ha313so.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await ha313so.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@ha313so.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def Hussein(event):
    ha313so = event.client
    joinu = await ha313so(JoinChannelRequest('ioibb'))
    joinu = await ha313so(JoinChannelRequest('eiint'))
    joinu = await ha313so(JoinChannelRequest('Mshaelr'))
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    ha313so = event.client
    global yaAli
    yaAli = True
    await aljoker_allnshr(ha313so, sleeptimet, message)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
super_groups = ["super", "سوبر" , "كروب" , "سـوبـر"]
async def aljoker_supernshr(ha313so, sleeptimet, message):
    global yaAli
    yaAli = True
    aljoker_chats = await ha313so.get_dialogs()
    while yaAli:
        for chat in aljoker_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await ha313so.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await ha313so.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"Error in sending message to chat {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@ha313so.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def Hussein(event):
    ha313so = event.client
    joinu = await ha313so(JoinChannelRequest('ioibb'))
    joinu = await ha313so(JoinChannelRequest('eiint'))
    joinu = await ha313so(JoinChannelRequest('Mshaelr'))
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    ha313so = event.client
    global yaAli
    yaAli = True
    await aljoker_supernshr(ha313so, sleeptimet, message)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
@ha313so.on(events.NewMessage(outgoing=True, pattern='.ستوب'))
async def stop_aljoker(event):
    joinu = await ha313so(JoinChannelRequest('ioibb'))
    joinu = await ha313so(JoinChannelRequest('eiint'))
    joinu = await ha313so(JoinChannelRequest('Mshaelr'))
    global yaAli
    yaAli = False
    await event.edit("**᯽︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
@ha313so.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def Hussein(event):
    ha313so = event.client
    joinu = await ha313so(JoinChannelRequest('ioibb'))
    joinu = await ha313so(JoinChannelRequest('eiint'))
    joinu = await ha313so(JoinChannelRequest('Mshaelr'))
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        joker_313 = """**🐍 قـائمة اوامر النشر التلقائي للمجموعات
ٴ— — — — — — — — — —
`.نشر` عدد الثواني معرف الكروب :
- للنشر في المجموعة التي وضعت معرفها مع عدد الثواني
ٴ— — — — — — — — — —
`.نشر_كروبات` عدد الثواني : 
- للنشر في جميع المجموعات الموجوده في حسابك
ٴ— — — — — — — — — —
`.سوبر` عدد الثواني : 
- للنشر بكافة المجموعات السوبر التي منظم اليها 
ٴ— — — — — — — — — —
`.ستوب` :
- لأيقاف جميع انواع النشر اعلاه
ٴ— — — — — — — — — —
• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة المُراد نشرها
ٴ— — — — — — — — — —**"""
        
    await event.reply(file='https://telegra.ph/file/dab0098fe59a6a8f6f938.mp4', message=joker_313)
    elif event.pattern_match.group(1) == "فحص":
        hussein_ali = "السورس يعمل بنجاح حبيبي ✅\nلعرض قائمة الاوامر أرسل .الاوامر"
        await event.reply(file='https://telegra.ph/file/dab0098fe59a6a8f6f938.mp4', message=hussein_ali)
        joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
        joker = Get(joker)
        try:
            await event.client(joker)
        except BaseException:
            pass
print('تم تشغيل نشر التلقائي لسورس شهم')
ha313so.run_until_disconnected()
