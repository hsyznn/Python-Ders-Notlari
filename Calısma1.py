"""
print(""""""--------------------<---------->------------
      
#Mükemmel Sayı hesaplama      
--------------------<---------->------------"""""")
sayi = int(input("Sayı Giriniz:"))
toplam = 0
for i in range(1,sayi):
    if (sayi % i == 0):
        toplam +=i
if(toplam == sayi):
    print("Mükemmel sayi")
else:
    print("Mükemmel sayi değil")
"""
"""
sayı = int(input("Sayı:"))

i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i += 1

if (toplam == sayı):
    print(sayı,"mükemmel bir sayıdır.")
else:
    print(sayı,"mükemmel bir sayı değildir.")

"""
"""
sayi = int(input("Sayı:"))
basamak = str(sayi)
toplam = 0
for x in basamak:
    üst = int(x)**len(basamak)
    toplam += üst
if (sayi == toplam):
    print("Armstong")
else:
    print("Armstong değil")
"""
"""
for i in range(1,11):
    print("************************")
    for j in range(1,11):
        print("{} * {} = {}".format(i,j,i*j))
"""
"""
toplam = 0
print("Çıkmak için 'q'ya basın")
while True:
    sayi = input("Sayı Giriniz:")
    if (sayi == "q"):
        break
    sayi = int(sayi)
    toplam += sayi
print("Toplam çıktı={}".format(toplam))
"""
"""
for i in range(1,101):
    if (i % 3 != 0):
        continue
    print(i)
"""
"""
list = [x for x in range (1,101) if x % 2 == 0]
print(list)
"""
"""
sayi1 = int(input("1.sayi:"))
sayi2 = int(input("2.sayı:"))
sayi3 = int(input("3.sayı:"))
if (sayi1 > sayi2) and (sayi1 > sayi3):
    print(sayi1,"En büyük sayı")
elif(sayi2 > sayi1) and (sayi2 > sayi3):
    print(sayi2,"En büyük sayı")
else:
    print(sayi3,"En büyük sayı")
"""
"""
sys_eposta = "huvigs43@gmail.com"
sys_sifre = "123321Huvi"
sayac = 3
while True:
    eposta = input("Eposta adresinizi girin:")
    sifre = input("Şifrenizi giriniz=")
    if (eposta != sys_eposta and sifre != sys_sifre):
        print("Eposta veya şifre yanlış.")
        sayac -=1
    elif (eposta == sys_eposta and sifre != sys_sifre):
        print("Sifre hatalı")
        sayac -=1
    elif(eposta != sys_eposta and sifre == sys_sifre):
        print("E-posta hatalı")
        sayac -=1
    else: 
        print("Giriş başarılı")
        break
    if (sayac == 0):
        print("Hakkınız doldu")
        break
"""
"""
notunuz = int(input("Notunuzu girin:"))
if (notunuz < 70):
    print("Belge alamazsınız.")
elif( notunuz < 85):
    print("Teşekkür aldınız")
else:
    print("takdir aldınız.")
"""
