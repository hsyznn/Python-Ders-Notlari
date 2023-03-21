"""
boy = float(input("Boyunuzu giriniz="))
kilo = float(input("Kilonuzu giriniz="))

indeks= kilo / boy ** 2
if indeks < 18.5:
    print("Zayıf")
elif indeks >= 18.5 and indeks <= 25:
    print("Normal")
elif indeks >= 25 and indeks <= 30:
    print("Fazla Kilolu")
else:
    print("obez")
"""
"""
sayı = float(input("1.sayı="))
sayı1 = float(input("2.sayı="))
sayı2 = float(input("3.sayı="))

if sayı >=  sayı1 and sayı >= sayı2:
    print("En büyük sayı {}".format(sayı))
elif sayı1 >= sayı and sayı1 >= sayı2:
    print("En büyük sayı={}".format(sayı))
elif sayı2 >= sayı and sayı2 >= sayı1:
    print("En büyük sayı={}".format(sayı2))
"""
"""
v1 = int(input("1.Vize notunuzu giriniz="))
v2 = int(input("2.Vize notunuzu giriniz="))
Final = int(input("Final notunuzu giriniz="))
toplam_not = v1 * 3/10 + v2 * 3/10 + Final * 4/10
if toplam_not >= 90 :
    print("Toplam Not = {} -----> AA".format(toplam_not))
elif toplam_not >= 85 :
    print("Toplam Not = {} -----> BA".format(toplam_not))
elif toplam_not >= 80:
    print("Toplam Not = {} -----> BB".format(toplam_not))
elif toplam_not >= 75 :
    print("Toplam Not = {} -----> CB".format(toplam_not))
elif toplam_not >= 70 :
    print("Toplam Not = {} -----> CC".format(toplam_not))
elif toplam_not >= 65 :
    print("Toplam Not = {} -----> DC".format(toplam_not))
elif toplam_not >= 60 :
    print("Toplam Not = {} -----> DD".format(toplam_not))
elif toplam_not >= 55 :
    print("Toplam Not = {} -----> FD".format(toplam_not))
else:
    print("FF")
"""
print("""---------<------->-------
Üçgen İçin 1 yazınız
Dikdörtgen için 2 yazınız
---------<------->-------""")
islem = input("İşlem seçiniz=")

if (islem =="2"):
    a = int(input("1.kenar:"))
    b = int(input("2.kenar:"))
    c = int(input("3.kenar:"))
    d = int(input("4.kenar:"))
    if (a == b and c == d):
        print("Şekliniz Kare")
    elif (a == c and b == d):
        print("Şekliniz Dikdörtgen")
    else:
        print("Şekliniz Dörtgen")

elif (islem == "1"):
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c ):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")
        
else:
    print("Geçersiz Şekil...")