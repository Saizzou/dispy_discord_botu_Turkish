#bot gereksinimleri
import discord
import dispy_varlar
import random
from discord.ext import commands
from datetime import datetime

TOKEN = dispy_varlar.TOKEN
# TOKEN'i saklamak için TOKEN'i başka bir dosyadan çektim.

client = discord.Client()
bot = commands.Bot(command_prefix='!') #Client yerine Subclass olan bot'u çağırıyoruz ve '!' ile komut çağrısı yapıyoruz.

with open('kotu_kelime.txt') as dosya: #Dosyayı doldurmanız gerekecek.
    dosya = dosya.read().split()


@bot.event #client.event yerine bot.event kullanıyoruz!
async def on_ready():
    print(f'{bot.user.name} bağlandı!')

    for guild in bot.get_all_members():
        print('Üye ve ID', end=":")
        print(f'{guild}')


@bot.event
async def on_member_join(member): #Kullanıcı katıldığında hoşgeldiniz mesajı oluşturur.
    await member.create_dm()
    await member.dm_channel.send(
        f'Merhaba {member.name}, Discord Kanalımıza Hoşgeldin!'
    )


@bot.command(name='bilgi', help='Botun kurucu bilgisini verir.')
#Ünlem (!komut) komut şeklinde çalışacak komutlar için kullanıyoruz örn: !bilgi

async def bilgi(ctx):
    bilgi_cvp = "Bu Bot Saizzou tarafından yapılmıştır. Botun yapılışı için github.com/Saizzou/dispy_discord_botu \
               adressine gidip botun kodlamasını inceleyebilirsiniz!"

    await ctx.send(bilgi_cvp)

@bot.command(name='zar_at', help='Zar atma simulasyonu !zar_at x y giriniz. Örneğin:'
                               '!zar_at 2 6 şeklinde.')
async def zar(ctx,zar_sayisi : int, zar_yuzu : int):
    zarlar = [ str(random.choice(range(1,zar_yuzu+1)))
               for _ in range(zar_sayisi)]
    await ctx.send(','.join(zarlar))

'''Örnek olsun diye bu şekilde yaptım yoksa normalde çift zar için: 
async def zar(ctx):
    zarlar = [ str(random.choice(range(1,7)))
               for _ in range(2)]
    await ctx.send(','.join(zarlar))
    şeklinde yapılabilirdi.'''

@bot.command(name='kanal_olustur',help='Kanal olusturur.')
@commands.has_role('Administrator')#Kanal oluşturma komutunu Administrator Grubuna verir.
@commands.has_role('Editör') #Kanal oluşturma komutunu Editör Grubuna verir.
async def kanal_olustur(ctx, yeni_kanal):
    guild = ctx.guild
    await guild.create_text_channel(yeni_kanal)

@bot.command(name='kick', help='Birilerini atmak icin kullanilir')
@commands.has_role('Administrator')
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)

@bot.event
async def on_message(message):
    kategoriler = ['python', 'genel-muhabbet'] #Botun olması istediğiniz kategorileri tam isimleriyle yazın.
    if str(message.channel) in kategoriler:
        if message.author == client.user:
            return  # Burası önemli bu kısmı unutursanız Bot kendi yazdığınada cevap verebilir.

        selam_verme_ornekleri = ['Selam Server\'imize hoşgeldin', 'Ooo kimleri görüyoruz', 'Ve aleyküm selam',
                                 'Merhabalar efenim', 'Birileri geri dönmüş bakıyorumda..', 'Dostum nerelerdeydin sen?']

        coklu = ['cok1', 'cok2', 'cok3'] #Buraya botun algılamasını istediğiniz kelimeleri girin
        coklu_cevap = ['cevap1', 'cevap2', 'cevap3', 'cevap4'] #Buraya cevap seçenekleri girin

        if message.content == 'selam':  # Bu kısım yüzde yüz bu şekilde olan mesaja cevap verir.
            cevap = random.choice(selam_verme_ornekleri)
            await message.channel.send(cevap)

        elif 'sorum' in message.content.lower():  # Bu kısım cümle içinde sözcük geçerse cevap verir.
            await message.channel.send('Sorularınız için Sorular kategorisine başvurabilirsiniz!')

        elif message.content.lower() in coklu:  # Bu kısım çoklu kelime algılama ve çoklu cevap döndürmeye yarar.
            cok_cevap = random.choice(coklu_cevap)
            await message.channel.send(cok_cevap)

        elif 'botu kim' in message.content.lower():
            await message.channel.send('Bu botu Saizzou yaptı. Beğendiysen sanada yapsın... ')  # Reklam :)

        for kotu_kelime in dosya:
            if kotu_kelime in message.content.lower():
                await message.delete()  # Kötü kelime barındıran mesajı siler
                await message.channel.send(
                    f'{message.author.mention}! Mesajınız kötü kelimeler yüzünden silinmiştir! UYARILDINIZ!')


    await bot.process_commands(message)  # Bunu unutursanız message command'ı override eder ve command çalışmaz!!!

bot.run(TOKEN)