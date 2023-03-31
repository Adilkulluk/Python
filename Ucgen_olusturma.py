sayi = input("Lütfen en az iki haneli tam bir sayı giriniz.")
ters_sayi = sayi[::-1]
sayi1 = int(sayi)
ters_sayi1 = int(ters_sayi)

if sayi1 % 2 == 0 and ters_sayi1 % 2 == 0:
    print("Çift-çift")
elif sayi1 % 2 == 0 and ters_sayi1 % 2 != 0:
    print("Çift-tek")
elif sayi1 % 2 != 0 and ters_sayi1 % 2 == 0:
    print("Tek-çift")
elif sayi1 % 2 != 0 and ters_sayi1 % 2 != 0:
    print("Tek-tek")

kenar1 = eval(input("Lütfen birinci kenarı giriniz: "))
kenar2 = eval(input("Lütfen ikinci kenarı giriniz: "))
kenar3 = eval(input("Lütfen üçüncü kenarı giriniz: "))

if kenar1 < kenar2 + kenar3 and kenar2 < kenar3 + kenar1 and kenar3 < kenar1 + kenar2:
    print("Üçgen oluşturulabilir.")
else:
    print("Üçgen oluşturulamaz")

