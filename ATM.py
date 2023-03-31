print("""***************************************
2ATM'ye Hoşgeldiniz....

İşlemler
1)Bakiye Sorgulama
2)Para Çekme
3)Para Yatırma

Çıkış yapmak için 'q' tuşuna basınız.
***************************************
""")
Bakiye = 1000
while True:
    işlem = input("İşlem seçiniz:")
    if işlem == "q" :
        print("Yine bekleriz....")
        break
    elif işlem == "1" :
        print("Bakiyeniz {} TL'dir".format(Bakiye))
        print("Başka işlem yapmak istiyor musunuz?")
        işlem = input("Lütfen işlemi giriniz:")
        if işlem == "Evet" :
            print("Lütfen bekleyiniz....")
        elif işlem == "Hayır" :
            print("Yine bekleriz....")
            break
        else :
            print("Geçersiz işlem. Çıkış yapılıyor....")
            break
    elif işlem == "2" :
        Miktar = int(input("Çekmek istediğiniz para tutarını giriniz"))
        if Bakiye - Miktar < 0 :
            print("Bakiyeniz yetersiz...")
            continue
        Bakiye -= Miktar
        print("{} Tl para çekilmiştir. Yeni bakiyeniz {} Tl'dir.".format(Miktar,Bakiye))
        print("Başka işlem yapmak istiyor musunuz?")
        işlem = input("Lütfen işlemi giriniz:")
        if işlem == "Evet":
            print("Lütfen bekleyiniz....")
        elif işlem == "Hayır":
            print("Yine bekleriz....")
            break
        else:
            print("Geçersiz işlem. Çıkış yapılıyor....")
            break
    elif işlem == "3" :
        Miktar1 = int(input("Yatırmak istediğiniz Tutarı giriniz."))
        Bakiye += Miktar1
        print("{} Tl para Yatırılmıştır. Yeni bakiyeniz {} Tl'dir.".format(Miktar1, Bakiye))
        print("Başka işlem yapmak istiyor musunuz?")
        işlem = input("Lütfen işlemi giriniz:")
        if işlem == "Evet":
            print("Lütfen bekleyiniz....")
        elif işlem == "Hayır":
            print("Yine bekleriz....")
            break
        else:
            print("Geçersiz işlem. Çıkış yapılıyor....")
            break
    else :
        print("Geçersiz işlem. Çıkış yapılıyor....")
        break