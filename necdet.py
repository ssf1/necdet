import csv


def ogrenci_listesi():
    liste = []
    with open("olcumler.csv", "r") as olcumler:
        reader = csv.DictReader(olcumler)
        for satir in reader:
            no = satir['proje no']
            isim = satir['isim']
            soyisim = satir['soy isim']
            okul = satir['okul']
            foto = satir['foto']
            with open("sonuclar.txt", "w") as sonuclar:
                print "Proje No:", " "*9, "isim"," "*21, "soyisim"," "*20, "okul"," "*20, "foto"
                print "-"*6, " ", "-"*20, " "*2, "-"*20, " "*3, "-"*20, " ", "-"*20, " "*2, "-"*20, " "*2, "-"*20
                print " ",no," "*5,isim," ",soyisim, okul, foto

ogrenci_listesi()


