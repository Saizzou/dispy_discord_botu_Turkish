# dispy_discord_botu
Örnek discord botu. Açıklamalar kod içinde mevcut
Gereken Kütüphaneler:
random
discord.py

discord.py için CMD komutu:
pip install -U discord.py
# -U: Upgrade demektir. Yani en son sürümleri eklemek için.

Discordunuza ait Developer bölümüne girip Token oluşturmanız gerekiyor. Bunun için:
http://discordapp.com/developers/applications
sayfasına gitmeniz gerekecektir.

Burdan 'New Application' seçin ve projenize bir isim verin.(Botada bu proje ismini verecektir ama değiştirebilirsiniz.)
Sonra Bot sekmesi altında 'Add Bot' kısmına tıklayın.
İzinleri oluşturun. (Deneme yapacaksanız hepsini verebilirsiniz.)
Token'ı burdan kopyalayabilirsiniz.

Botu Discorda eklemek için OAuth2 kısmına gelin ve alt kısımda bulunan Bot Kutucuğunu işaretleyin.
Üstteki Url'yi kopyalayıp Web Tarayıcınızın Adress Bölümüne yapıştırıp enter'e basın.
Hangi Server'e ekleme yapmak istediğinizi soracaktır. (Botu birden fazla Server'de çalıştırabilirsiniz.)

# client.py ile client uygulaması yaptık
# dispy.py ile bot uygulaması yaptık

Client ile bot arasındaki fark bot Client'in subclassı olduğu için client'a göre daha geniş bir yelpazeye sahiptir.
