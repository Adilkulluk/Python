import math
import time

class PC():

    def __init__(self,pc_durum = "Kapalı", ses_ayarlari = 0, kamera_durumu = "kapalı", tarayici_listesi = ["Explorer"],):
        self.pc_durum = pc_durum
        self.ses_ayarlari = ses_ayarlari
        self.kamera_durumu = kamera_durumu
        self.tarayici_listesi = tarayici_listesi
    def pc_ac(self):
        if self.pc_durum == "Açık":
            print("Bilgisayar zaten açık.....")
        else:
            print("Bilgisayarınız açılıyor......")
            self.pc_durum = "Açık"
    def pc_kapa(self):
        if self.pc_durum == "Kapalı":
            print("Bilgisayar zaten kapalı.....")
        else:
            print("Bilgisayarınız kapatılıyor......")
            self.pc_durum = "Kapalı"
    def ses(self):
        while True:
            cevap = input("Sesi azaltmak için '-' tuşuna basınız.\nSesi arttırmak için '+' tuşuna basınız.\nÇıkış yapmak için 'exit' yazınız.")
            if cevap == "+":
                if self.ses_ayarlari != 31:
                    self.ses_ayarlari += 1
                    print("Ses yükseltildi. Yeni ses:",self.ses_ayarlari)
            elif cevap == "-":
                if self.ses_ayarlari != 0:
                    self.ses_ayarlari -= 1
                    print("Ses azaltıldı. Yeni ses:",self.ses_ayarlari)
            else:
                print("Çıkış yapılıyor. Güncel ses:",self.ses_ayarlari)
                break

    def kamera_ac(self):
        if self.kamera_durumu == "Açık":
            print("Kameranız zaten açık.....")
        else:
            print("Kameranız açılıyor.....")
            self.kamera_durumu = "Açık"

    def kamera_kapa(self):
        if self.kamera_durumu == "Kapalı":
            print("Kameranız zaten kapalı.....")
        else:
            print("Kameranız kapatılıyor......")
            self.kamera_durumu = "Kapalı"

    def tarayici_ekle(self, tarayici_ismi):
        print("Tarayıcı ekleniyor.....")
        time.sleep(1)
        self.tarayici_listesi.append(tarayici_ismi)
        print("Tarayıcılar eklendi. Tarayıcılarınız:",self.tarayici_listesi)

    def __str__(self):
        return "Pc Durumu: {}\nSes Seviyesi: {}\nKamera Durumu: {}\nTarayıcılar: {}".format(self.pc_durum, self.ses_ayarlari, self.kamera_durumu, self.tarayici_listesi)

PC = PC()

print("""
PC Uygulaması

1)PC aç
2)PC kapa
3)Ses ayarları
4)Kamera aç
5)Kamera kapat
6)Tarayıcı ekle
7)Tarayıcı sayısı öğrenme
8)Genel bilgiler

Çıkış yapmak için 'q' tuşuna basınız.
""")

while True:
    islem = input("Lütfen işleminizi giriniz:")

    if islem == "q":
        print("Çıkış yapılıyor.")
        break
    elif islem == "1":
        PC.pc_ac()
    elif islem== "2":
        PC.pc_kapa()
    elif islem == "3":
        PC.ses()
    elif islem == "4":
        PC.kamera_ac()
    elif islem == "5":
        PC.kamera_kapa()
    elif islem == "6":
        tarayici_adi = input("Tarayıcı isimlerini ',' koyarak yazınız.")
        tarayici_listesi = tarayici_adi.split(",")
        for eklenecekler in tarayici_listesi:
            PC.tarayici_ekle(eklenecekler)
    elif islem == "7":
        print("Tarayıcı sayınız:", len(tarayici_listesi)+ 1)
    elif islem == "8":
        print(PC)
    else:
        print("HATALI İŞLEM......")