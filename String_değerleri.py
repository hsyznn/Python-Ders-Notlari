"""
print("hüseyin Özen")
"""
#("") noktalamasından 3 tane de koyabiliriz.
#print("""hüseyin Özen""")
#--------<------>-------------------------------
#Hatalı işlem
"""
print("hüseyin Özen')
"""
# print("""hüseyin Özen')
#            ^
#SyntaxError: invalid syntax
#print('Hüseyin'in')  hata verecektir doğrusu
"""
print("Hüseyin'in") veya
"""
"""
print('Hüseyin\'in') \ işareti kaçış için kullanılır yani o anlamda değil, bu o demek değil gibi
"""
#İndesklemele
"""
a = "Hüseyin"
print("çikti=", a[4])
"""
#sondan İndeskleme
"""
a = "Hüseyin"
print("çikti=", a[-4])
"""
#*[başlama indeksi : bitiş indeksi : atlama değeri]*
"""
a = "Hüseyin Özen"
print("çikti=", a[0:4])
"""
"""
a = "Hüseyin Özen"
print("çikti=", a[0:4:2])
"""
#uzunluk hesaplama
"""
a = "hüseyin"
print("uzunluk=", len(a))
"""