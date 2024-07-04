import json

class HarcamaTablosu:
    def __init__(self):
        self.harcamalar = []
        self.toplam_borclar = {}
        self.veritabani = "harcamalar.json"
        self.kisi_sayisi = 6  
        self.veritabani_yukle()

    def veritabani_yukle(self):
        try:
            with open(self.veritabani, "r") as file:
                data = json.load(file)
                self.harcamalar = data.get("harcamalar", [])
                self.toplam_borclar = data.get("toplam_borclar", {})
        except FileNotFoundError:
            print("Veritabanı bulunamadı. Yeni bir veritabanı oluşturulacak.")

    def veritabani_kaydet(self):
        with open(self.veritabani, "w") as file:
            data = {
                "harcamalar": self.harcamalar,
                "toplam_borclar": self.toplam_borclar
            }
            json.dump(data, file, indent=4)

    def harcama_ekle(self, kisi, tutar, aciklama):
        self.harcamalar.append((kisi, tutar, aciklama))
        self.toplam_borclar[kisi] = self.toplam_borclar.get(kisi, 0) - tutar
        self.veritabani_kaydet()

    def harcamalari_goster(self):
        if not self.harcamalar:
            print("Henüz yapılan harcama bulunmamaktadır.")
        else:
            print("Harcama Listesi:")
            for i, harcama in enumerate(self.harcamalar, start=1):
                print(f"{i}. Harcama Yapan: {harcama[0]}, Tutar: {harcama[1]} TL, Açıklama: {harcama[2]}")

            self.toplam_alacaklar()

    def toplam_alacaklar(self):
        print("\nToplam Alacaklar:")
        for kisi, borc in self.toplam_borclar.items():
            if borc < 0:
                print(f"{kisi}: {abs(borc)} TL alacak")

    def odeme_tutari(self, kisi):
        if kisi in self.toplam_borclar:
            print(f"\n{self.kisi_sayisi} kişi için {kisi}'in alacağı miktar: {abs(self.toplam_borclar[kisi])} TL")
            kisi_basi_odeme = abs(self.toplam_borclar[kisi]) / self.kisi_sayisi
            print(f"Geri kalan kişi başı ödeme tutarı: {kisi_basi_odeme:.2f} TL")

if __name__ == "__main__":
    harcama_tablosu = HarcamaTablosu()

    while True:
        print("\nYapılan işlemi seçin:")
        print("1. Harcama Ekle")
        print("2. Harcamaları Göster")
        print("3. Kişinin Alacağını ve Geri Kalan Kişi Başına Ödeme Tutarını Göster")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == '1':
            print("\nYapılan harcama için bilgileri girin:")
            kisi = input("Harcama yapan kişinin adı: ")
            tutar = float(input("Harcama tutarı (TL): "))
            aciklama = input("Harcama açıklaması: ").strip() 
            harcama_tablosu.harcama_ekle(kisi, tutar, aciklama)
        elif secim == '2':
            print("\n--- Harcama Listesi ---")
            harcama_tablosu.harcamalari_goster()
        elif secim == '3':
            kisi = input("\nKişinin adını girin: ")
            harcama_tablosu.odeme_tutari(kisi)
        elif secim == '4':
            print("\nProgramdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
