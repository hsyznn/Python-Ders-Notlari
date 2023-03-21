print ("""--------------<-------->--------      
       Kullanıcı Giriş Paneli       
--------------<-------->--------""")
sys_kullanici ="Admin"
sys_sifre ="Admin123"
hak = 3
while True:
    kul = input("Kullanıcı Adı:")
    sif = input("Şifre:")
    if (kul != sys_kullanici and sif != sys_sifre):
        print("Şifre ve kullanıcı adı yanlış.")
        hak -= 1
    elif(kul == sys_kullanici and sif !=sys_sifre):
        print("Şifreniz Hatalı")
        hak -=1
    elif(kul != sys_kullanici and sif ==sys_sifre):
        print("Kullanıcı adı hatalı Hatalı")
        hak -=1
    else:
        print("Giriş Başarılı")
        break
    if (hak == 0):
        print("hakkınız bitti")
        break