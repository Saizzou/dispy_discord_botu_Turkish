#bot gereksinimleri
import discord
import dispy_varlar
import random

TOKEN = dispy_varlar.TOKEN
#TOKEN'i saklamak için TOKEN'i başka bir dosyadan çektim.
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(f'{client.user} bağlandı! Server ID: {guild.id}')
        #Unutmayın ki Discord Serverleri Guild olarak tanımlar!

        kullanicilar = '\n - '.join([member.name for member in guild.members])
        print(f'Server Kullanıcıları:\n - {kullanicilar}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Merhaba {member.name}, Discord Kanalımıza Hoşgeldin!'
    )

@client.event
async def on_message(message):
    kategoriler = ['python','genel-muhabbet','Allgemein']
    if str(message.channel) in kategoriler:
        if message.author == client.user:
            return #Burası önemli bu kısmı unutursanız Bot kendi yazdığınada cevap verebilir.

        selam_verme_ornekleri = ['Selam Server\'imize hoşgeldin', 'Ooo kimleri görüyoruz', 'Ve aleyküm selam',\
                                'Merhabalar efenim','Birileri geri dönmüş bakıyorumda..', 'Dostum nerelerdeydin sen?' ]

        coklu = ['cok1','cok2','cok3']
        coklu_cevap = ['cevap1','cevap2','cevap3','cevap4']

        if message.content == 'selam': #Bu kısım yüzde yüz bu şekilde olan mesaja cevap verir.
            cevap = random.choice(selam_verme_ornekleri)
            await message.channel.send(cevap)

        elif 'sorum' in message.content.lower(): #Bu kısım cümle içinde sözcük geçerse cevap verir.
            await message.channel.send('Sorularınız için Sorular kategorisine başvurabilirsiniz!')

        elif message.content.lower() in coklu: #Bu kısım çoklu kelime algılama ve çoklu cevap döndürmeye yarar.
            cok_cevap = random.choice(coklu_cevap)
            await message.channel.send(cok_cevap)

        elif 'botu kim' in message.content.lower():
            await message.channel.send('Bu botu Saizzou yaptı. Beğendiysen sanada yapsın... ') #Reklam :)


client.run(TOKEN)