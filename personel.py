class Personel:
    def __init__(self,personel_no,ad,soyad,departman,maas):
        self._personel_no = personel_no
        self._ad = ad
        self._soyad = soyad
        self._departman = departman
        self._maas = maas
    def get_personel_no(self):
        return self._personel_no
    def get_ad(self):
        return self._ad
    def get_soyad(self):
        return self._soyad
    def get_departman(self):
        return self._departman
    def get_maas(self):
        return self._maas
    def set_personel_no(self,girdi):
        self._personel_no = girdi
    def set_ad(self,girdi):
        self._ad = girdi
    def set_soyad(self,girdi):
        self._soyad = girdi
    def set_departman(self,girdi):
        self._departman = girdi
    def set_maas(self,girdi):
        self._maas = girdi
    def __str__(self):
        return f"Ad: {self._ad}, Soyad: {self._soyad}, Personel No: {self._personel_no}, Departman: {self._departman}, Maas: {self._maas}"