"""
break ifadesi döngülerde programcılar tarafından en çok kullanılan ifadedir. Anlamı şu şekildedir;

            Döngü herhangi bir yerde ve herhangi bir zamanda break ifadesiyle karşılaştığı zaman
            çalışmasını bir anda durdurur. Böylelikle döngü hiçbir koşula bağlı kalmadan sonlanmış olur.
            
            
break ifadesi **sadece ve sadece** içindeki bulunduğu döngüyü sonlandırır. Eğer iç içe döngüler bulunuyorsa ve en içteki döngüde break kullanılmışsa sadece içteki döngü sona erer. Örneklerle *break* ifadesini anlamaya çalışalım.
"""
"""
sayi = 0
while (sayi < 20):
    if(sayi == 10):
        break
    print("Sayi:",sayi)
    sayi += 1
"""
"""
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    if (i == 6):
        break
    print("Sayı:",i)
"""
"""
while True:
    isim = input("isminizi Giriniz(Çıkmak için 'w''ya basınız.):")
    if (isim == "W" or isim == "w"):
        print("Program durduruldu...")
        break
    print("İsmiz:",isim)
"""
"""
### continue ifadesi
*continue* ifadesi *break*'e göre biraz daha az kullanılan bir ifadedir. Anlamı şu şekildedir;
            
        Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığı zaman geri kalan işlemlerini
        yapmadan direk bloğunun başına döner.
        
*continue* ifadesini anlamak için örneklerimize bakalım.
"""
list = list(range(11))
print(list)
for i in list:
    if(i == 5 or i == 10):
        continue
    print("Sayı:",i)