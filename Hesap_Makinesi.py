print("""---------------<------------->------------
Hesap Makinesi
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
1-4'e kadar bir işlem seçin=   
---------------<------------->------------""")
islem = input("İşleminizi Giriniz:")
if islem =="1":
    a = float(input("1.sayı="))
    b = float(input("2.sayı="))
    sonuc= a + b
    print("{} + {}={}".format(a,b,sonuc))
elif islem =="2":
    a = float(input("1.sayı="))
    b = float(input("2.sayı="))
    sonuc= a - b
    print("{} - {}={}".format(a,b,sonuc))
elif islem =="3":
    a = float(input("1.sayı="))
    b = float(input("2.sayı="))
    sonuc= a * b
    print("{} * {}={}".format(a,b,sonuc))
elif islem =="4":
    a = float(input("1.sayı="))
    b = float(input("2.sayı="))
    sonuc= a / b
    print("{} / {}={}".format(a,b,sonuc))
else:
    print("Yukarıda belirtilen işlemlerden birisini seçiniz!")