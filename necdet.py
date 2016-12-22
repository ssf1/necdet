import csv

siralar = []

isimler_ler = []
isimler = []
isimler2 = []

danismanlar = []

okullar_lar = []
iller = []
okullar = []

alanlar = []

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
            isimler.append(isim1)



# okul ve sehirleri ayirdik
    for i in okullar_lar:
        il, okul_ad = i.split(" ",1)
        iller.append(il)

# okul sonundaki kacis dizisinden kurtulduk
    for i in okullar_lar:
        okul_isim = i.split("\n")[0]
        okullar.append(okul_isim)







csv_ayirici()

liste_ayiklayici()


print (siralar)
print (isimler)
print (isimler2)
print (danismanlar)
print (iller)
print (okullar)
print (alanlar)


