import time

kullanici_adi = "Türkiye"
sifre = 1923
while True:
    isim = input("Kullanıcı adınızı giriniz.")
    parola = int(input("Şifrenizi giriniz."))
    if (isim != kullanici_adi and sifre == parola) or (isim == kullanici_adi and sifre != parola):
        print("Bilgileriniz kontrol ediliyor lütfen bekleyiniz....")
        time.sleep(1)
        print("Kullanıcı adınız veya şifreniz yanlış. Tekrar deneyiniz.")
    elif (isim != kullanici_adi) and (sifre != parola):
        print("Bilgileriniz kontrol ediliyor lütfen bekleyiniz....")
        time.sleep(1)
        print("Kullanıcı adınız veya şifreniz yanlış. Tekrar deneyiniz.")
    else:
        print("Bilgileriniz kontrol ediliyor lütfen bekleyiniz....")
        time.sleep(1)
        print("Kullanıcı adı ve şifreniz doğru giriş yapıldı.")
        break