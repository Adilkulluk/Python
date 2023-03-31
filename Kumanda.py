import random
import time


class kumanda():

    def __init__(self, tv_durum ="kapalı", tv_ses = 0, kanal_listesi =  ["TRT"], kanal= "TRT", renkler = ["Kırmızı"]):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.renkler = renkler
    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyonunuz zaten açık.....")
        else:
            print("Televizyonunuzu açılıyor.....")
            self.tv_durum = "Açık"
    def tv_kapa(self):
        if self.tv_durum == "Kapalı":
            print("Televizyonunuz zaten kapalı.....")
        else:
            print("Televizyonunuz kapatılıyor.....")
            self.tv_durum = "Kapalı"
    def ses_ayarlari(self):
        while True:
            cevap = input("ses azaltmak için '<'\narttırmak için '>'\nçıkış için 'exit' yazınız.")

            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses azaltıldı. Ses seviyesi:", self.tv_ses)
            elif cevap == ">":
                if self.tv_ses != 31:
                    self.tv_ses += 1
                    print("Ses arttırıldı. Ses seviyesi:", self.tv_ses )
            else:
                print("Güncel ses: ", self.tv_ses)
                break
    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor.....")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi. Kanallarınız: ", self.kanal_listesi)

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal: ", self.kanal)
    def renk_ekle(self, eklenecek_renkler):
        print("Renkler ekleniyor.....")
        time.sleep(1)
        self.renkler.append(eklenecek_renkler)
        print("Renkler eklendi. Renkleriniz", self.renkler)


    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "TV Durumu: {}\nTV Ses: {}\nKanal Listesi: {}\nŞu anki Kanal: {}\nRenklerimiz: {}".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal, self.renkler)
kumanda = kumanda()
print("""
Televizyon uygulaması

1)Tv aç
2)Tv kapat
3)Ses ayarları
4)Kanal ekle
5)Kanal sayısını öğrenme
6)Rastgele kanala geçme
7)Renkler
8)Televizyon bilgileri

Çıkmak için 'q' ya basınız
""")


while True:
    islem = input("İşleminizi seçiniz:")

    if islem == "q":
        print("Uygulamadan çıkış yapılıyor......")
        break
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapa()
    elif islem == "3":
        kumanda.ses_ayarlari()
    elif islem == "4":
        kanal_isimleri = input("Kanal isimlerini ',' koyarak giriniz:")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif islem == "5":
        print("Kanal sayısı:", len(kumanda))
    elif islem == "6":
        kumanda.rastgele_kanal()
    elif islem == "8":
        print(kumanda)
    elif islem == "7":
        yazilanrenkler = input("Renkleri ',' koyarak giriniz:")
        renkler = yazilanrenkler.split(",")
        for eklenenrenkler in renkler:
            kumanda.renk_ekle(eklenenrenkler)
    else:
        print("HATALI İŞLEM.....")