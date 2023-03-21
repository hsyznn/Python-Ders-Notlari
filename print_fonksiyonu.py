"""
print(34,23.32,"Hüseyin")
"""
#"34 23.32 Hüseyin" şeklinde boşluklı çıkıyor
#Stringdeki özel karakterler
"""
print("Hüseyin\nÖzen")
"""
#Hüseyin
#Özen
#Stringdeki \t tab(4) kadar boşluk bırakıyor
"""
print("Hüseyin\tÖzen\t2002")
"""
#Hüseyin Özen    2002
#----------------<---------->------------------
#veri tipini öğrenme
"""
a=23
print(type(a))
"""
#<class 'int'>
"""
b="Hüseyin"
print(type(b))
#<class 'str'>
"""
#"sep" parametresi boşluk yerine gelmesini istediğimiz şeyi yazar.
"""
print(1,2,3,4,5,sep=",")
"""
#1,2,3,4,5
"""
a = "13"
b = "07"
c = "2002"
print(a,b,c,sep="/")
"""
#13/07/2002
"""
print("hüseyin","Berat","Emir",sep="\n") 
"""
#alt altya yazar
#--------------------------<------------>----------------------
#"*" parametresi harflerin arasına boşluk ekler
"""
print(*"Hüseyin")
"""
#H ü s e y i n
"""
print(*"Hüseyin",sep="/")
"""
#H/ü/s/e/y/i/n
#Programlama yaparken bazı yerlerde bir stringin içinde daha önceden tanımlı string,float, int vs. değerleri yerleştirmek isteyebiliriz.
#Böyle durumlar için Pythonda *format()* fonksiyonu bulunmaktadır.
#Örneğin, programımızda 3 tane tamsayı değerimiz var ve biz bunları bir string içinde ekrana basmak istiyoruz.
#Bunun için *format()* fonksiyonunu kullanabiliriz. 
#*format()* fonksiyonunun çok fazla özelliği olduğu için, ben burada sadece en çok kullandığımız özelliğini göstereceğim.
"""
print("{} {} {}".format(3.23,234.34,452.234))
"""
#3.23 234.34 452.234
"""
a = 100
b = 4
print("{} sayısı ile {}'e bölümü = {}'tür".format(a,b,a // b))
#100 sayısı ile 4'e bölümü = 25'tür
"""
#Numaralandırma 0'dan başlar
"""
print("Doğum Tarihim: {2}/{0}/{1}".format("Temmuz",2002,13))
"""
#Doğum Tarihim: 13/Temmuz/2002
#ondalıklı sayının sadece 2 basamağını alıyor
"""
print("{:.2f} {:.2f} {:.2f}".format(3.14634,4.3423,6.4923))
"""
#3.15 4.34 6.49