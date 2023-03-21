"""
list = [1,2,3,"elma",5,6]
print(list)
"""
"""
list = [1,2,3,"elma",5,6]
print(type(list))
#<class 'list'>
"""
#listler boş olabilir
"""
list = []
print(list)
#Çıktı "[]""
"""
# bir diğer boş list oluşturma yöntemi
"""
list = list()
print(list)
# Çıktı "[]"
"""
#list() fonksiyonu listeye dönüştürebilir
"""
list = list("Hüseyin")
print(list,len(list), sep="\n")
#['H', 'ü', 's', 'e', 'y', 'i', 'n']
#7
"""
#indeksleme
"""
list = [1,2,3,4,5,6,7,8,9,10]
print(list[2])
#Çıktı "3"
"""
#sonuncu veriyi alma
"""
list = [1,2,3,4,5,6,7,8,9,10]
print("Sonuç=", list[len(list)-1])
#Sonuç= 10
"""
#Listler parçalanabilir
"""
list = [1,2,3,4,5,6,7,8,9,10]
print("Sonuç=", list[2:5])
#Sonuç= [3, 4, 5]
"""
#Listler toplanabiliyor
"""
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print("Sonuç=", list1 + list2)
#Sonuç= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
"""
list1 = [1,2,3,4]
list2 = list1 * 3
print("Sonuç=", list2)
#Sonuç= [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
"""
#Stringlerde değerler değişemezken listlerde değişiyor.
"""
list = [1,2,3,4]
list[1] = 20
print("Sonuç=", list)
#Sonuç= [1, 20, 3, 4] 
"""
#listleri parçalayarak değişterebiliriz.
"""
list = [1,2,3,4,5]
list[:3] = [10,20,30]
print("Sonuç=", list)
#Sonuç= [10, 20, 30, 4, 5]
"""
#Append methodu sayesinde listeye değer ekleyebiliriz.
"""
list = [1,2,3,4,5,6]
list.append("Hüseyin")
print("Sonuç=",list)
#Sonuç= [1, 2, 3, 4, 5, 6, 'Hüseyin']
"""
#pop methodu ile listeden değer çıkarabiliriz.
""""
list = [1,2,3,4,5,6]
list.pop(4)
print("Sonuç=", list)
#Sonuç= [1, 2, 3, 4, 6]
"""
#sort methodu sıralama methodu
"""
list = [1,23,25,44,70,230,100]
list.sort
print("Sonuç=", list)
#Sonuç= [1, 23, 25, 44, 70, 230, 100]
"""
#tersten sıralama(Büyükten Küçüğe)
"""
list = [1,23,25,44,70,230,100]
list.sort(reverse= True)
print("Sonuç=", list)
#Sonuç= [230, 100, 70, 44, 25, 23, 1]
"""
#alfabetik sıralama
"""
list = ["Hüseyin","Özen","Berat","Mami","Emir","Talha"]
list.sort()
print("Sonuç=", list)
#Sonuç= ['Berat', 'Emir', 'Hüseyin', 'Mami', 'Talha', 'Özen']
"""
#tersten alfabetik sıralama
"""
list = ["Hüseyin","Özen","Berat","Mami","Emir","Talha"]
list.sort(reverse=True)
print("Sonuç=", list)
#Sonuç= ['Özen', 'Talha', 'Mami', 'Hüseyin', 'Emir', 'Berat']
"""
#iç içe listler oluşabiliyor
"""
list = [ [1,2], [3,4], ["hüseyin","Özen"]]
print("Sonuç=",list)
#Sonuç= [[1, 2], [3, 4], ['hüseyin', 'Özen']]
"""
#iç içe listler parçalanabilir
"""
list = [ [1,2], [3,4], ["hüseyin","Özen"]]
print("Sonuç=",list[1] [0])
"""