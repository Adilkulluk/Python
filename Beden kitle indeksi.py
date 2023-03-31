print("""************************
      HOŞGELDİNİZ
************************
""")

Kilo = int(input("Kilonuzu giriniz:"))
Boy = float(input("Boyunuzu giriniz"))
Beden_kitle_indeksi = Kilo / (Boy * Boy)
print(Beden_kitle_indeksi)
if Beden_kitle_indeksi < 18.5 :
    print("Zayıf")
elif 18.5 <= Beden_kitle_indeksi < 25 :
    print("Normal")
elif 25 <= Beden_kitle_indeksi < 30 :
    print("Fazla kilolu")
else:
    print("Obez")