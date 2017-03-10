# coding=utf-8
import csv

siralar = []                        # proje nolar
isimler_ler = []                    # proje yapan ogrenci isimleri (ayni proje de 1 den cok isim olabilir)
isimler = []                        # ogrenci isimleri ayri ayri yazildi (nested list olarak)
danismanlar = []                    # danisman isimleri
okullar_lar = []                    # sehir ve okul isimleri
iller = []                          # sehir isimleri ayrildi
okullar = []                        # okul isimleri sehirle birlikte temiz olarak yazildi
alanlar = []                        # proje dallari

ogr_kartlari = []
danisman_kartlari = []

def csv_ayirici():
    with open('tubitak_listesi.csv', "r") as liste:
        reader = csv.DictReader(liste)
        for satir in reader:
            sira = satir['sıra']
            bas_no = satir['BAŞVURU NO']
            isim = satir['ÖĞRENCİ ADI SOYADI']
            danisman = satir['DANIŞMAN ADI SOYADI']
            okul = satir['OKULU']
            proje = satir['PROJENİN ADI']
            alani = satir['ALANI']

            siralar.append(sira)
            isimler_ler.append(isim)
            danismanlar.append(danisman)
            okullar_lar.append(okul)
            alanlar.append(alani)


def liste_ayiklayici():

# ayni hucreden aldigi isimleri ayirdik
    for i in isimler_ler:
        isim1, isim2 = i.split("\n")
        if isim2 != '':
            isimler.append([isim1,isim2])
        else:
            isimler.append([isim1])
# okul ve sehirleri ayirdik
    for i in okullar_lar:
        il, okul_ad = i.split(" ",1)
        iller.append(il)
# okul sonundaki kacis dizisinden kurtulduk
    for i in okullar_lar:
        okul_isim = i.split("\n")[0]
        okullar.append(okul_isim)


def ogrenciler():
    for i in range(len(siralar)):
        if len(isimler[i]) > 1 :
            for j in range(len(isimler[i])):
#                print (siralar[i])
#                print (isimler[i][j])
#                print (iller[i])
#                print (alanlar[i])
#                print (okullar[i])
                ogr_kartlari.append([siralar[i], isimler[i][j], iller[i], alanlar[i], okullar[i]])
        else:
#            print (siralar[i])
#            print (isimler[i][0])
#            print (iller[i])
#            print (alanlar[i])
#            print (okullar[i])
            ogr_kartlari.append([siralar[i], isimler[i][0], iller[i], alanlar[i], okullar[i]])


def danisman():
    for i in range(len(siralar)):
#        print (siralar[i])
#        print (danismanlar[i])
#        print (iller[i])
#        print (alanlar[i])
#        print (okullar[i])
        danisman_kartlari.append([siralar[i], danismanlar[i], iller[i], alanlar[i], okullar[i]])


csv_ayirici()
liste_ayiklayici()
ogrenciler()
danisman()


print (ogr_kartlari)
print (danisman_kartlari)

print (len(ogr_kartlari))
print (len(danisman_kartlari))

"""
# kart sayisinin tek mi cift mi oldugunu kontrol ederek cift sayi yapiyoruz
if len(ogr_kartlari) % 2 != 0:
    ogr_kartlari.append([])
"""

# ogrenci yaka kartlarini yazdiriyoruz

with open("ogrenci_kartlari.html", "w") as ogr:
    print (
        """
<html>
<head>
    <meta charset="utf-8">
    <title>Öğrenci yaka kartları </title>
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
    <div id = "wrapper" >
        """, file=ogr)

    i = 0
    while i < len(ogr_kartlari):
        print("""
    <div id = "kart" >
        <div id = "isimlik" class = "box">
            <div id ="logoluk" class = "box">
                <div id ="logo">
                    <img name="logo" src="logo_tubitak.jpg" alt="tubitak_logosu">
                </div>
                <div id ="proje">
                    <p>Proje No</p>
                    <div id = "no">
            """, file=ogr)

        print(ogr_kartlari[i][0], file = ogr)

        print("""
                    </div>
                </div>
            </div>
            <div id = "ic_isimlik" class = "box">
                <div id = "etkinlik">
                    <p>48. ORTAÖĞRETİM ÖĞRENCİLERİ</P>
                    <p>ARAŞTIRMA PROJELERİ BÖLGE YARIŞMALARI</p>
                </div>
                <div id = "tarih">
                    <p> 22-24 MART 2016 / VAN </p>
                </div>
                <div id = "yazi">
                    <p> ÖĞRENCİ</p>
                </div>
                <div id = "ogr_isim">
                    <p>
            """, file=ogr)

        print(ogr_kartlari[i][1], file = ogr)

        print("""
                    </p>
                </div>
                <div id = "il_dal" class="box">
                    <div id = "il">
                        <p>
            """, file=ogr)

        print(ogr_kartlari[i][2], file = ogr)

        print("""
                        </p>
                    </div>
                    <div id = "dal">
                        <p>
            """, file=ogr)

        print(ogr_kartlari[i][3], file = ogr)

        print("""
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div id = "ogr_okul" class = "box">
            <p>
            """, file=ogr)

        print(ogr_kartlari[i][4], file = ogr)

        print("""
            </p>
        </div>
    </div>
        """, file=ogr)
        i = i+1

    print ( """
    </div>
</body>
</html>
        """, file=ogr)



#danisman yaka kartlarini yazdiriyoruz

with open("danisman_kartlari.html", "w") as dan:
    print (
        """
<html>
<head>
    <meta charset="utf-8">
    <title>Danışman yaka kartları </title>
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
        """, file=dan)

    i = 0
    while i < len(danisman_kartlari):
        print("""
    <div id = "kart_dan">
        <div id = "isimlik_dan" class = "box">
            <div id ="logoluk" class = "box">
                <div id ="logo">
                    <img name="logo" src="logo_tubitak.jpg" alt="tubitak_logosu">
                </div>
                <div id ="proje">
                    <p>Proje No</p>
                    <div id = "no">
            """, file=dan)

        print(danisman_kartlari[i][0], file = dan)

        print("""
                    </div>
                </div>
            </div>
            <div id = "ic_isimlikdan" class = "box">
                <div id = "etkinlik">
                    <p>48. ORTAÖĞRETİM ÖĞRENCİLERİ</P>
                    <p>ARAŞTIRMA PROJELERİ BÖLGE YARIŞMALARI</p>
                </div>
                <div id = "tarih">
                    <p> 22-24 MART 2016 / VAN </p>
                </div>
                <div id = "yazi">
                    <p> DANIŞMAN</p>
                </div>
                <div id = "dan_isim">
                    <p>
            """, file=dan)

        print(danisman_kartlari[i][1], file = dan)

        print("""
                    </p>
                </div>
                <div id = "il_dal" class="box">
                    <div id = "il">
                        <p>
            """, file=dan)

        print(danisman_kartlari[i][2], file = dan)

        print("""
                        </p>
                    </div>
                    <div id = "dal">
                        <p>
            """, file=dan)

        print(danisman_kartlari[i][3], file = dan)

        print("""
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div id = "dan_okul"  class = "box">
            <p>
            """, file=dan)

        print(danisman_kartlari[i][4], file = dan)

        print("""
            </p>
        </div>
    </div>
        """, file=dan)
        i = i+1

    print ( """
    </div>
</body>
</html>
        """, file=dan)




