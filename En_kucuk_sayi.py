sayi1 = eval(input("Birinci sayıyı giriniz: "))
sayi2 = eval(input("İkinci sayıyı giriniz: "))
sayi3 = eval(input("Üçüncü sayıyı giriniz: "))

if sayi1 < sayi2 and sayi1 < sayi3:
    print("En küçük sayınız: ", sayi1)
elif sayi2 < sayi1 and sayi2 < sayi3:
    print("En küçük sayınız:", sayi2)
elif sayi3 < sayi1 and sayi3 < sayi2:
    print("En küçük sayınız:", sayi3)