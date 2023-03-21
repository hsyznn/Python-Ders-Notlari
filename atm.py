print("""------------------<------------>------------
      ATM'ye hoş geldiniz.
      Para sorgulamak için 1'i
      Para Yatırmak için 2'yi
      Para Çekmek için 3'ü
      ATM'den çıkmak için 4'ü seçiniz.      
------------------<------------>------------""")
bakiye = 100
while True:
    islem = input("İşlem Seçiniz:")
    if (islem == "4"):
        print("ATM'den çıkış yapıldı.")
        break
    elif (islem == "1"):
        print("Bakiyeniz:",bakiye)
    elif (islem == "2"):
        Miktar = int(input("Yatırmak istediğiniz miktarı girin:"))
        bakiye += Miktar
        print("Güncel Miktar:",bakiye)
    elif (islem == "3"):
        Miktar = int(input("Çekmek istediğiniz miktarı giriniz:"))
        bakiye -= Miktar
        print("Güncel Bakiye:",bakiye)
        if (bakiye - Miktar < 0):
            print("Yetersiz bakiye")
            continue
    else:
        print("Geçersiz işlem")
        