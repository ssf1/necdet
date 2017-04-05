# coding=utf-8
import csv

isimler = []                        # isimleri ayri ayri yazildi (nested list olarak)
gorevler = []                       # gorevleri yazildi

personel_kartlari = []
juri_kartlari = []

def csv_ayirici():
    with open('personel.csv', "r") as liste:
        reader = csv.DictReader(liste)
        for satir in reader:
            isim = satir['ad soyad']
            gorev = satir['görev']

            isimler.append(isim)
            gorevler.append(gorev)

def personeller():
    for i in range(len(isimler)):
#        print (siralar[i])
#        print (danismanlar[i])
#        print (iller[i])
#        print (alanlar[i])
#        print (okullar[i])
        personel_kartlari.append([isimler[i], gorevler[i]])


csv_ayirici()
personeller()


print (personel_kartlari)

print (len(personel_kartlari))



"""
# kart sayisinin tek mi cift mi oldugunu kontrol ederek cift sayi yapiyoruz
if len(ogr_kartlari) % 2 != 0:
    ogr_kartlari.append([])
"""


#personel yaka kartlarini yazdiriyoruz

with open("personel_kartlari.html", "w") as per:
    print (
        """
<html>
<head>
    <meta charset="utf-8">
    <title>Personel yaka kartları </title>
    <link rel = "stylesheet" href="style.css" type = "text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="z-50L0HFIXAJjH6yeYrnQIRhy6-cNnQkvCZo1ZdkgL0" />
    <!--[if IE]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
    <!--[if lte IE 7]>
    <script src="js/IE8.js" type="text/javascript"></script><![endif]-->
    <!--[if lt IE 7]>
    <link rel="stylesheet" type="text/css" media="all" href="css/ie6.css"/><![endif]-->
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"> </script>
</head>

<body>
    <div id = "wrapper">
        """, file=per)

    i = 0
    while i < len(personel_kartlari):
        print("""
    <div id = "kart_per">
        <div id = "isimlik_per" class = "box">
            <div id ="logoluk" class = "box">
                <div id ="logo">
                    <img name="logo" src="logo_tubitak.jpg" alt="tubitak_logosu">
                </div>
                <div id ="proje">
                    <p>&nbsp;</p>
                    <div id = "no">&nbsp;</div>
                </div>
            </div>
            <div id = "ic_isimlikper" class = "box">
                <div id = "etkinlik">
                    <p>11. ORTAOKUL ÖĞRENCİLERİ</P>
                    <p>ARAŞTIRMA PROJELERİ</p>
                    <p> YARIŞMASI</p>
                </div>
                <div id = "tarih">
                    <p> 17-20 NİSAN 2017 / VAN </p>
                </div>

                <div id = "per_isim">
                    <p>
            """, file=per)

        print(personel_kartlari[i][0], file = per)

        print("""
                    </p>
                </div>
                <div id = "il_dal" class="box">
                    <div id = "il">
                        <p> &nbsp; </p>
                    </div>
                    <div id = "dal">
                        <p> &nbsp; </p>
                    </div>
                </div>
            </div>
        </div>
        <div id = "per_gorev"  class = "box">
            <p>
            """, file=per)

        print(personel_kartlari[i][1], file = per)

        print("""
            </p>
        </div>
    </div>
        """, file=per)
        i = i+1

    print ( """
    </div>
</body>
</html>
        """, file=per)




