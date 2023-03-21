"""
yas = int(input("Yaşınızı Giriniz:"))
if (yas >= 18):
    print("Ehliyet alabiliriniz:")
else:
    print("Ehliyet alamazsınız:")
    """
"""
for i in range(1,101):
    if (i % 2 == 0):
        print("çift sayılar:",i)
"""
"""
for i in range(1,101):
    if (i % 3 == 0) or (i % 5 == 0):
        print("Sonuç:",i)
"""
"""
sayi=input('Sayıyı Gir : ')
for i in range(1,int(sayi)+1):
  print(i)
"""
"""
k1 = int(input("1.kenar"))
k2 = int(input("2.kenar"))

alan= k1 * k2hü
cevre = 2 * (k1+k2)
print("alan:",alan)
print("çevre:",cevre)
"""
"""
metin = input("Kelime girin:")
sayac = 0
while (sayac < len(metin)):
    print(metin[sayac])
    sayac +=1       
    """
"""
say1 = int(input("sayı giriniz:"))
say2 = int(input("sayı giriniz:"))
toplam = 0
for i in range((say1)+1,say2):
    toplam +=i
    print(toplam)
"""
"""
tercih = input("Sinema için 1'i, Tiyatro için 2'yi seçiniz:")
ogrenci = input("Öğrenci için 1'i, Öğrenci Değilseniz 2'yi seçiniz:")
toplam = 0
if (tercih == "1"):
    toplam = 15
    
elif (tercih == "2"):
    toplam = 10
    
if (ogrenci == "1"):
    toplam = toplam // 2
print("Ödemeniz gereken ücret :{}".format(toplam))
"""
"""
sayac = 0
sayi = int(input("sayi giriniz:"))
for i in range(2,int(sayi)):
    if int(sayi) % i == 0:
        sayac +=1
        
if (sayac != 0):
    print("Asal sayı")
else:
    print("asal sayı değil")
"""
"""
boy = float(input("Boyunuzu Giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))

vki = kilo / boy**2
if (vki <= 18):
    print("İndeksiniz {} Normal".format(vki))
elif (vki <= 18) and (vki <=25):
    print("indeksiniz {} kilolu".format(vki))
elif (vki > 25) and  (vki <=30):
    print("İndeksiniz {} obez".format(vki))
elif (vki > 30):
    print("İndeksiniz {} ciddi obez".format(vki))
    """
"""
yas = input("Yaşınızı Giriniz=")
if (yas >= "18"):
    print("Ehliyet Alabilirsiniz")
else:
    print("Ehliyet Alamazsınız")
"""
"""
for i in range(1,101):
    print("sonuç=",i)
"""

"""
for i in range(1,101):
    if (i % 2 == 0):
        print(i)
        """
"""
for i in range(1,101):
    if (i % 2 != 0):
        print(i)
        """
"""
for i in range(1,101):
    if (i % 3 == 0) or (i % 5 == 0):
        print(i)
"""
"""
sayi = input("Sayı girinz:")
for i in range(1,int(sayi)):
    print(i)
"""
"""
metin = input("Kelime Giriniz:")
sayac = 0
while (sayac < len(metin)):
    print(metin[sayac])
    sayac +=1
"""
"""
s1 = input("Sayı Giriniz:")
s2 = input("Sayı Giriniz:")
toplam  = 0
for i in range(int(s1)+1,int(s2)):
    toplam +=i
    print(toplam)
"""
"""maas = input("Maaşınızı Giriniz:")
zam = input("Zam oranını giriniz:")
yeni_maas = int(maas) + int(maas) * int(zam) / 100
print("Maaşınız:",yeni_maas)
"""
"""
sayi = input("sayı giriniz:")
tektoplam = 0
cifttoplam= 0
for i in range(1,int(sayi)):
    if (i % 2 == 0):
        
        cifttoplam += i
    else:
        tektoplam += i
print("Tek toplam= ",tektoplam)
print("Çift toplam= ", cifttoplam)
"""
"""
cap = input("Dairenin yarı çapını giriniz:")
cev = 2 * 3.14 * float(cap)
alan = 3.14 * float(cap)*float(cap)
print("Dairenin Alanı:",alan,"Dairenin Çevresi:",cev)
"""