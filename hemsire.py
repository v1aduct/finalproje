import personel

class Hemsire(personel.Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self._calisma_saati = calisma_saati
        self._sertifika = sertifika

    def get_calisma_saati(self):
        return self._calisma_saati
    def get_sertifika(self):
        return self._sertifika
    def set_calisma_saati(self, value):
        self._calisma_saati = value
    def set_sertifika(self, value):
        self._sertifika = value

    def maas_arttir(self,oran):
        self._maas = self._maas * (1+oran)


    def __str__(self):
        return (f"Ad: {self._ad}, Soyad: {self._soyad}, Personel No: {self._personel_no}, "
                f"Departman: {self._departman}, Maas: {self._maas}, Calisma Saati: {self._calisma_saati}, "
                f"Sertifika: {self._sertifika}")
    

