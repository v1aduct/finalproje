class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self._hasta_no = hasta_no
        self._ad = ad
        self._soyad = soyad
        self._dogum_tarihi = dogum_tarihi
        self._hastalik = hastalik
        self._tedavi = tedavi

    def get_hasta_no(self):
        return self._hasta_no
    def get_ad(self):
        return self._ad
    def get_soyad(self):
        return self._soyad
    def get_dogum_tarihi(self):
        return self._dogum_tarihi
    def get_hastalik(self):
        return self._hastalik
    def get_tedavi(self):
        return self._tedavi
    def set_hasta_no(self, girdi):
        self._hasta_no = girdi
    def set_ad(self, girdi):
        self._ad = girdi
    def set_soyad(self, girdi):
        self._soyad = girdi
    def set_dogum_tarihi(self, girdi):
        self._dogum_tarihi = girdi
    def set_hastalik(self, girdi):
        self._hastalik = girdi
    def set_tedavi(self, girdi):
        self._tedavi = girdi

    def tedavi_suresi_hesapla(self):
        tedavi_sureleri = {
            "Gribal Enfeksiyon": 7,
            "Bronşit": 14,
            "Pnömoni": 21,
            "Migren": 10,
            "Hipertansiyon": 30,
            "Diyabet": 30,
            "Kanser": 180,
            "Kalp Hastalığı": 90,
            "Astım": 30,
            "Mide Ülseri": 14
        }
        return tedavi_sureleri.get(self._hastalik, 10)

    def __str__(self):
        return (f"Ad: {self._ad}, Soyad: {self._soyad}, Hasta No: {self._hasta_no}, "
                f"Dogum Tarihi: {self._dogum_tarihi}, Hastalik: {self._hastalik}, Tedavi: {self._tedavi}")
    
    