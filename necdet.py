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
            sira = int(satir['sıra'])
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

# kart sayisinin tek mi cift mi oldugunu kontrol ederek cift sayi yapiyoruz
if len(ogr_kartlari) % 2 != 0:
    ogr_kartlari.append([])


with open("ogrenci_kartlari.html", "w") as ogr:
    i = 0
    while i < 16:
        print (i, "\t" * 25, i+1 , file = ogr, end="\n")
        print (ogr_kartlari[i], "\t" * 6, ogr_kartlari[i+1], file = ogr, end="\n")
        i = i+2

