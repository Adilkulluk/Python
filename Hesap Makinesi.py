print("""****************************************
-------------Hesap Makinesi-------------
1) Toplama İşlemi
2) Çıkarma İşlemi
3) Çarpma İşlemi
4) Bölme İşlemi
****************************************
""")
sayı1 = int(input("Birinci sayıyı giriniz:"))
sayı2 = int(input("İkinci sayıyı giriniz:"))
Yapılacak_işlem = int(input("Hangi işlemi yapmak istiyorsunuz:"))

if Yapılacak_işlem == 1:
    print("{} ile {} toplamı {} yapar".format(sayı1,sayı2,sayı1+sayı2))
elif Yapılacak_işlem == 2:
    print("{} ile {} farkı {} yapar".format(sayı1,sayı2,sayı1-sayı2))
elif Yapılacak_işlem == 3:
    print("{} ile {} çarpımı {} yapar".format(sayı1,sayı2,sayı1 * sayı2))
elif Yapılacak_işlem == 4:
    print("{} ile {} bölümü {} yapar".format(sayı1,sayı2,sayı1 / sayı2))
else:
    print("Geçersiz Değer!..")