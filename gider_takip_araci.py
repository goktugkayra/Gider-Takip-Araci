import csv

GIDERLER_DOSYASI = "giderler.csv"

def giderleri_yukle():
    try:
        with open(GIDERLER_DOSYASI, "r") as dosya:
            okuyucu = csv.DictReader(dosya)
            return list(okuyucu)
    except FileNotFoundError:
        return []

def giderleri_kaydet(giderler):
    with open(GIDERLER_DOSYASI, "w", newline="") as dosya:
        yazici = csv.DictWriter(dosya, fieldnames=giderler[0].keys())
        yazici.writeheader()
        yazici.writerows(giderler)

def gider_takip_araci():
    giderler = giderleri_yukle()

    while True:
        print("Gider Takip Aracı")
        print("1. Giderleri Listele")
        print("2. Yeni Gider Ekle")
        print("3. Çıkış")

        secim = input("Seçiminizi yapın (1-3): ")

        if secim == "1":
            if giderler:
                print("Giderler:")
                for gider in giderler:
                    print(f"Tarih: {gider['Tarih']}, Kategori: {gider['Kategori']}, Miktar: {gider['Miktar']} TL")
            else:
                print("Henüz gider kaydı bulunmamaktadır.")
        elif secim == "2":
            tarih = input("Gider tarihini girin (GG.AA.YYYY): ")
            kategori = input("Gider kategorisini girin: ")
            miktar = input("Gider miktarını girin (TL): ")

            gider = {"Tarih": tarih, "Kategori": kategori, "Miktar": miktar}
            giderler.append(gider)

            giderleri_kaydet(giderler)
            print("Yeni gider kaydedildi.")
        elif secim == "3":
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

gider_takip_araci()
