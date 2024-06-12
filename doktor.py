import personel 

class Doktor(personel.Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self._uzmanlik = uzmanlik
        self._deneyim_yili = deneyim_yili
        self._hastane = hastane

    def get_uzmanlik(self):
        return self._uzmanlik
    def get_deneyim_yili(self):
        return self._deneyim_yili
    def get_hastane(self):
        return self._hastane
    def set_uzmanlik(self, girdi):
        self._uzmanlik = girdi
    def set_deneyim_yili(self, girdi):
        self._deneyim_yili = girdi
    def set_hastane(self, girdi):
        self._hastane = girdi

    def maas_arttir(self,oran):
        self._maas = self._maas * (1+oran)
    
    def __str__(self):
        return (f"Ad: {self._ad}, Soyad: {self._soyad}, Personel No: {self._personel_no}, "
                f"Departman: {self._departman}, Maas: {self._maas}, Uzmanlik: {self._uzmanlik}, "
                f"Deneyim Yili: {self._deneyim_yili}, Hastane: {self._hastane}")

