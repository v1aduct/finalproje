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
