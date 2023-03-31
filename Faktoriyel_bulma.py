print("""************************************************
Faktoriyel bulma programına hoşgeldiniz

Çıkış yapmak için q tuşuna basınız
************************************************
""")

while True:
    sayı = input("sayı giriniz")
    if(sayı == "q"):
        print("Program sonlandırılıyor.....")
        break

    else:
        sayı = int(sayı)
        faktoriyel = 1
        for i in range(2,sayı+1):
            faktoriyel *= i
        print("faktoriyel",faktoriyel)