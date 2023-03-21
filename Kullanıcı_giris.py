"""
kullanici = input("Kullanıcı adı:")
sifre = input("Şifre:")
print("------------------<------>-------------")
if kullanici == "Admin" and sifre == "123321Huvi":
    print("Hoşgeldiniz!")
else:
    print("şifre ve ya kullanıcı adı yanlış!")
"""
"""
sys_kullanici_adi= "Admin"
sys_sifre="123321Huvi"

kullanici = input("Kullanıcı adı:")
sifre = input("Şifre:")
if kullanici != sys_kullanici_adi and sifre != sys_sifre:
    print("Giriş Başarısız")
elif kullanici != sys_kullanici_adi and sifre == sys_sifre:
    print("Giriş Başarısız")
elif kullanici == sys_kullanici_adi and sifre != sys_sifre:
    print("Giriş başarısız")
else:
    print("Giriş Başarılı! Hoşgeldiniz!")
"""
