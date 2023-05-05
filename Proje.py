# Toplantıda konuştugumuz gibi kullanıcı verileri için txt dosyası yazmakla başlıyorum. @sara

class Kisi:
    def __init__(self, kimlik_no, ad_soyad, dogum_yili, cinsiyet, oncelik_durumu):
        self.kimlik_no = kimlik_no
        self.ad_soyad = ad_soyad
        self.dogum_yili = dogum_yili
        self.cinsiyet = cinsiyet
        self.oncelik_durumu = oncelik_durumu

    def __str__(self):
        return f"Kimlik No: {self.kimlik_no}\nAd Soyad: {self.ad_soyad}\nDoğum Yılı: {self.dogum_yili}\nCinsiyet: {self.cinsiyet}\nÖncelik Durumu: {self.oncelik_durumu}\n"
    @classmethod
    def kaydet(cls, kisiler, Kisi_Bilgileri):
        with open(f"{Kisi_Bilgileri}.txt", 'a', encoding="utf-8") as dosya:
            for kisi in kisiler:
                dosya.write(str(kisi))
                dosya.write('\n')

kisiler = []

while True:
    print("Bilgileri giriniz veya çıkmak için 'q' girin:")
    kimlik_no = input("Kimlik No: ")
    if kimlik_no == 'q':
        break
    ad_soyad = input("Ad Soyad: ")
    dogum_yili = input("Doğum Yılı: ")
    cinsiyet = input("Cinsiyet: ")
    oncelik_durumu = input("Öncelik Durumu(-7 & +65 Yaş/ Engelli/ Şehit-Gazi Yakınlık/ Randevulu/ Hamile /Yok): ")
    
    kisi = Kisi(kimlik_no, ad_soyad, dogum_yili, cinsiyet, oncelik_durumu)
    kisiler.append(kisi)

Kisi.kaydet(kisiler, 'Kisi_Bilgileri')

