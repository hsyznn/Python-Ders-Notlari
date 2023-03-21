#in operatörü bir elemanın başka bir listede olup olmadığını konrtrol eder.
"""
print("a" in "merhaba")
#True
print("a" in "berber")
#False
"""
"""
list = [1,2,3,4,5]
for eleman in list:
    print(eleman)
#1
#2
#3
#4
#5
"""
"""
toplam = 0
list = [1,2,3,4,5]
for eleman in list:
    toplam = toplam + eleman
    print("Toplam={} Eleman={}".format(toplam,eleman))
    Toplam=1 Eleman=1
#çıktı
Toplam=3 Eleman=2
Toplam=6 Eleman=3
Toplam=10 Eleman=4
Toplam=15 Eleman=5
"""
"""
list = [1,2,3,4,5,6,10,12,13,17,18,20,35,65,43,94,34,30]
for eleman in list:
    if (eleman % 2 == 0):
        print("Çift Sayılar:{}".format(eleman))
    if (eleman % 2 != 0):
        print("Tek sayılar={}".format(eleman))
"""
"""
tuple = (1,2,3,4,5)
for eleman in tuple:
    print(eleman)
"""
"""
list = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for (i,j) in list:
    print("Sonuç:{}".format(i*j))
"""
"""
dict = {"Bir":1, "İki":2, "Üç":3}
for (i,j) in dict.items():
    print("Anahtar:{}".format(i),"Değer:{}".format(j))
"""
liste = [2,1,10,2,23,1,56,3]
 
total = 0
for i in liste:
    if (not (i % 2 == 0)):
        total += i
 
print(total)