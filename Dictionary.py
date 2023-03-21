#Dictionary(Sözlükler) gerçek hayattaki sözlüklere benzer
"""
dict = {"Bir":1, "iki":2}
print("Çıktı=", type(dict))
#Çıktı= <class 'dict'>
"""
#Dictler boş olabilir
"""
dict = dict()
print("Sonuç=", dict)
#Sonuç= {}
"""
#Dictleri bulma
"""
dict = {"Bir":1, "İki":2, "Üç":3}
print("Çıktı=", dict ["Bir"])
#Çıktı= 1
"""
#Dictlere key ekleyebiliriz
"""
dict = {"Bir":1, "İki":2, "Üç":3,}
dict ["Dört"] = 4
print("Çıktı", dict)
#Çıktı {'Bir': 1, 'İki': 2, 'Üç': 3, 'Dört': 4}
"""
"""
a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
print("Çıktı=", a["iki"])
#Çıktı= [[1, 2], [3, 4], [5, 6]]
"""
"""
b = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
print("Çıktı=", b["iki"] [1] [:1])
#Çıktı= [3]
"""
#Dictler değiştirebilir
"""
b = {"Bir": [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
b["Bir"] [2] = 6
print("Çıktı=", b["Bir"])
#Çıktı= [1, 2, 6, 4]
"""
#İç İçe Dictler
"""
dict = {"Takımlar":{"Galatasaray":"GS","Beşiktaş":"Bjk","Fenerbahçe":"Fb","Trabzon":"TS"}, "Kuruluş":{"Galatasaray":1905,"Beşiktaş":1903,"Fenerbahçe":1907,"Trabzonspor":1967}}
print("Çıktı=", dict["Takımlar"] ["Galatasaray"], dict ["Kuruluş"] ["Galatasaray"])
#Çıktı= GS 1905
"""
#Dict_key methodu key verir

"""
dict = {"Takımlar":{"Galatasaray":"GS","Beşiktaş":"Bjk","Fenerbahçe":"Fb","Trabzon":"TS"}, "Kuruluş":{"Galatasaray":1905,"Beşiktaş":1903,"Fenerbahçe":1907,"Trabzonspor":1967}}
print("Çıktı=", dict.keys())
#Çıktı= dict_keys(['Takımlar', 'Kuruluş'])
"""
#Dict_Values ise keyin karşılığını verir
"""
dict = {"Takımlar":{"Galatasaray":"GS","Beşiktaş":"Bjk","Fenerbahçe":"Fb","Trabzon":"TS"}, "Kuruluş":{"Galatasaray":1905,"Beşiktaş":1903,"Fenerbahçe":1907,"Trabzonspor":1967}}
print("Çıktı=", dict.values())
#Çıktı= dict_values([{'Galatasaray': 'GS', 'Beşiktaş': 'Bjk', 'Fenerbahçe': 'Fb', 'Trabzon': 'TS'}, {'Galatasaray': 1905, 'Beşiktaş': 1903, 'Fenerbahçe': 1907, 'Trabzonspor': 1967}])
"""
#Dict_items methodu ile Tuple(Demetler) şeklinde alabiliriz
"""
dict = {"Bir":1, "İki":2, "Üç":3,}
print("Çıktı=", dict.items())
#Çıktı= dict_items([('Bir', 1), ('İki', 2), ('Üç', 3)])
"""