"""
ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı:")
takım = input("Oyuncunun takımı:")

bilgiler = [ad,soyad,takım]

print("Bilgiler Kaydediliyor....")

print("Oyuncunun Adı:{}\n Oyuncunun soyadı:{}\n Oyuncunun takımı:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi.")
"""
"""
a = int(input("Birinci Kökü giriniz="))
b = int(input("İkinci Kökü giriniz="))
c = int(input("üçüncü kökü giriniz="))

delta = b ** 2 - 4 * a * c 

a1 = (-b - delta ** 0.5) / (2*a)
b2 = (-b + delta ** 0.5) / (2*a)
print("Birinci Kök={}\nİkinci Kök={}\n".format(a1,b2))
"""
"""
a = int(input("1.sayıyı giriniz="))
b = int(input("2.sayıyı giriniz="))
c = int(input("3.sayıyı giriniz="))

çarp = (a*b) * c
print("Sonuç={}".format(çarp))
"""
"""
boy = float(input("Boyunuzu giriniz="))
kilo = int(input("Kilonuzu giriniz="))

kitle = kilo / (boy ** 2)

print("Kitle İndeksi={}".format(kitle))
"""
"""
a = float(input("Km'de kaç kuruş yakıyor:"))
b = int(input("Kaç km yol yaptınız:"))

hesap = a * b
print("Ödemeniz gereken tutar={} TL".format(hesap))
"""
"""
ad = input("Adınızı Giriniz=")
soyad = input ("Soyadınızı Giriniiz=")
numara = int(input("Numaranızı Giriniz=))
print("İsiminiz={}\nSoyisiminiz={}\nNumaranız=".format(ad,soyad,numara))
"""
"""
s1 = int(input("1.Sayıyı Giriniz:"))
s2 = int(input("2.Sayıyı Giriniz:"))
print("Girilen Sayılar= {},{}".format(s1,s2))
print("Sayılar değişiyor...")
s1,s2 = s2,s1
print("1.sayı={}\n2.sayı={}".format(s1,s2))
"""
"""
k1 = int(input("1.kenarı giriniz="))
k2 = int(input("2.kenarı giriniz="))

Hipo= (k1**2 + k2**2) ** 0.5
print("Üçgenin Hipotenüsü={}".format(Hipo))
"""
