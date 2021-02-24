import discord
import bilgi
import random
from discord.ext import commands
from datetime import datetime
import time


TOKEN = bilgi.TOKEN

client = discord.Client()
bot = commands.Bot(command_prefix='!')

with open('kufur.txt') as kufurler:
    kufurler = kufurler.read().split()


# Baglanilan Server'e ait Üye Bilgilerini Terminale aktar
@bot.event
async def on_ready():
    print(f'{bot.user.name} baglandi!')

    for server in bot.get_all_members():
        print('Üye ve ID', end=":")
        print(f'{server}')

#Yeni Katilan Kullaniciya Hosgeldin Mesaji
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Koddunyam Discord Kanalina Hosgeldin {member.name}! '
    )

@bot.event
async def giris_yapan_var(member):
    await client.send_message(member, newUserDMMessage)
    await client.send_message(discord.Object(id='CHANNELID'), 'Hosgeldin!! Sorulari http://forum.koddunyam.net üzerinden sorabilirsin! Burda da 10 Numara muhabbet dönüyor haberin olsun!!!')

#Bilgilendirme Komutu
@bot.command(name='bilgi', help='Bot bilgilendirmesi')
async def bilgi(ctx):
    bilgi_cvp = "Bu Bot Koddunyam Discord Kanalinin Karsilama Botudur!"
    await ctx.send(bilgi_cvp)

# !kufuret yazildiginda olacak olan islem:
@bot.command(name='kufuret', help='Botun Kufur etmesini saglar')
async def kufur(ctx):
    kufur_cvp = "Seni tinkyler sonra winkylerim"
    await ctx.send(kufur_cvp)

# !zar-at denilince rastgele 2 zar ciktisi verir.
@bot.command(name='zar-at', help='Zar oyunu')
async def zar_at(ctx):
    a = random.choice(range(1,7))
    b = random.choice(range(1,7))
    zar = f'Sansina cikan zarlar: {a} ve {b}'
    await ctx.send(zar)

# !topla sayi1 sayi2 ile toplama islemi yapmasini saglar
@bot.command(name='topla',a=int,b=int,help="Toplama islemi yapmasini saglar")
async def topla(ctx,a:int,b:int):
    await ctx.send(a+b)

@bot.command()
async def sec(ctx, *sec:str):
    await ctx.send(random.choice(sec))

# !metin_kanali komutu ile yeni metin kanali acar
@bot.command(name='metin_kanali', help='Metin Kanali olusturur')
@commands.has_role('Coder')
async def metin_kanali(ctx, metin):
    server = ctx.guild
    await server.create_text_channel(metin)

# !ses_kanali ile yeni ses kanali acar
@bot.command(name='ses_kanali', help='Ses Kanali olusturur')
@commands.has_role('Administrator')
async def ses_kanali(ctx, ses):
    server = ctx.guild
    await server.create_voice_channel(ses)

# Administrator yetkisi olan kullanicilarin !kick kullanici_adi komutu ile kullanici atmasini saglar
@bot.command(name='kick', help= 'Birisini atmak icin kullan')
@commands.has_role('Administrator')
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)


# Bot'un konusmalarda olusacak olan mesaj iceriklerine cevap vermesini saglar
@bot.event
async def on_message(message): # Botun hangi kanallardaki konusmalara bakmasi gerektigini belirler 

    if message.author == client.user:
        return

    selam_alma = ['Sa','Selam','s.a','sa','slm','selam']
    bot_selamlama = ['Aleyna Aleyküm esselam', 'Ooooooo kimleri görüyorum', 'Vaaaaaay Sen yasiyor muydun ya?','Vay a.s Haci cav cav , nörüyon?', 'A.s ne geziyon buralarda?','Selamina selam cigerim!','Bana selam verme selam tutmayi... Yok yok konular karisti.. A.s','Dedi naber dedim iyidir... A.s genc!','Merhabalar, Koddunyam.net Discord Kanalina Hosgeldiniz... NÖRÜYON Cigerparem?']
    
    if 'mikael kim' in message.content.lower():
        await message.channel.send('ADAM Kodun icinden geciyor öyle bi abimizdir! ')

    if message.content.lower() in selam_alma:
        selam_ver = random.choice(bot_selamlama)
        await message.channel.send(selam_ver)

    if 'bot' in message.content.lower():
        await message.channel.send('Sssssss Bu konu forum.koddunyam.net harici tartisilmamalidir!')
        if message.author == client.user:
            return

    elif 'özel ders' in message.content.lower():
        await message.channel.send('ssssss Ozel ders Konusu acilinca Saizzou sövüyor!')
        if message.author == client.user:
            return

    for kufur in kufurler:
        if kufur in message.content.lower():
            await message.delete()
            msg = f'{message.author.mention}! Kufur edeni tinkywinkylerim aklin basina gelir!'
            await message.channel.send(msg)


    await bot.process_commands(message)
bot.run(TOKEN)
