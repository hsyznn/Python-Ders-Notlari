print("""-----------------<--------->
    Pizza Sipariş Programı
    Küçük(S) Boy Pizza:25 TL
    Orta(M)  Boy Pizza:30 TL
    Büyük(B) Boy Pizza:35 TL
---------------<----------->""")
secim = input("Pizza Seçiniz:")
peynir = input("Ekstra Peynir Olsun mu?(E\H):")
icecek = input("İçecek Olsun mu?(E/H):")

hesap = 0
if (secim == "S" or secim =="s"):
    hesap +=25
elif (secim == "M" or secim == "m"):
    hesap +=30
else:
    hesap +=35
if (peynir == "E" or peynir =="e"):
    if (secim =="S"):
        hesap +=2
    else:
        hesap +=3   
if (icecek == "E" or icecek =="e"):
    hesap +=2
print("Toplam Tutar={}".format(hesap))