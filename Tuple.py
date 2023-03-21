#Tuple(demetler) değiştirelemez
"""
tuple = (1,2,3,4,5,6)
tuple [3] = 20
print("Çıktı=", tuple)
"""
#Hata kodu
#'tuple' object does not support item assignment
#File "C:\Users\husey\Desktop\pythoncode\Tuple.py", line 42, in <module>
#tuple [3] = 20
#TypeError: 'tuple' object does not support item assignment
"""
tuple = (1,2,3,4,5)
print("Çıktı=", type(tuple))
#Çıktı= <class 'tuple'>
"""
#Tuple içindeki verilere erişme
"""
tuple = (1,2,3,4,5,6)
print("Çıktı=",tuple[3])
#Çıktı= 4
"""
"""
tuple = (1,2,3,4,5,6)
print("Çıktı=",tuple[:3])
#Çıktı= (1, 2, 3)
"""
#Tuplenin içinde bulunan verilerin kaç defa geçtiğini görebiliriz
"""
tuple = (21,21,21,21,33,33,55,5,5,5,)
print("Çıktı=", tuple.count(21))
#Çıktı= 4
"""
#Tuplenin içinde olmayan bir veri verildiğinde
"""
tuple = (21,21,21,21,33,33,55,5,5,5,)
print("Çıktı=", tuple.count(6))
#Çıktı= 0
"""
#İndex methodu ile verinin kaçıncı index olduğunu söyler
"""
tuple = ("Hüseyin","Özen",13,"Temmuz")
print("Çıktı=", tuple.index("Temmuz"))
#Çıktı= 3
"""
"""
tuple = ("Hüseyin","Özen",13,"Temmuz")
print("Çıktı=", tuple.index(13))
#Çıktı= 2
"""