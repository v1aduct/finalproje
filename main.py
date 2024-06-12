from personel import Personel
from doktor import Doktor
from hemsire import Hemsire
from hasta import Hasta
import pandas as pd

print("Personeller: \n")

personel1 = Personel(1, "Ali", "Demir", "Resepsiyon", 25000)
personel2 = Personel(2, "Ayşe", "Yılmaz", "Temizlik", 20000)

print(personel1)
print(personel2)

print("\nDoktorlar: \n")

doktor1 = Doktor(3, "Ali", "Kaya", "Kardiyoloji", 80000, "Kardiyolog", 10, "Hastane A")
doktor2 = Doktor(4, "Ayşe", "Demir", "Ortopedi", 75000, "Ortopedist", 8, "Hastane B")
doktor3 = Doktor(5, "Mehmet", "Yılmaz", "Nöroloji", 82000, "Nörolog", 12, "Hastane C")

print(doktor1)
print(doktor2)
print(doktor3)

print("\nHemsireler: \n")

hemsire1 = Hemsire(6, "Ayşe", "Yılmaz", "Acil Servis", 45000, 40, "Acil Yardım Sertifikası")
hemsire2 = Hemsire(7, "Fatma", "Kaya", "Cerrahi Servis", 48000, 38, "Yara Bakım Sertifikası")
hemsire3 = Hemsire(8, "Mehmet", "Demir", "Yoğun Bakım", 50000, 36, "Yoğun Bakım Sertifikası")

print(hemsire1)
print(hemsire2)
print(hemsire3)

print("\nHastalar: \n")

hasta1 = Hasta(1, "Ali", "Yılmaz", "1980-05-15", "Diyabet", "İlaç Tedavisi")
hasta2 = Hasta(2, "Ayşe", "Demir", "1975-09-20", "Kanser", "Kemoterapi")
hasta3 = Hasta(3, "Mehmet", "Kaya", "1990-12-10", "Astım", "İnhaler Tedavi")

print(hasta1)
print(hasta2)
print(hasta3)



personel_data = {
    "Ad": ["Ali", "Ayse"],
    "Soyad": ["Demir", "Yilmaz"],
    "Personel No": [1, 2],
    "Departman": ["Resepsiyon", "Temizlik"],
    "Maas": [25000, 20000]
}


doktor_data = {
    "Ad": ["Ali", "Ayşe", "Mehmet"],
    "Soyad": ["Kaya", "Demir", "Yılmaz"],
    "Personel No": [1, 2, 3],
    "Departman": ["Kardiyoloji", "Ortopedi", "Nöroloji"],
    "Maas": [8000, 7500, 8200],
    "Uzmanlik": ["Kardiyolog", "Ortopedist", "Nörolog"],
    "Deneyim Yili": [10, 8, 12],
    "Hastane": ["Hastane A", "Hastane B", "Hastane C"]
}


hemsire_data = {
    "Ad": ["Ayşe", "Fatma", "Mehmet"],
    "Soyad": ["Yılmaz", "Kaya", "Demir"],
    "Personel No": [1, 2, 3],
    "Departman": ["Acil Servis", "Cerrahi Servis", "Yoğun Bakım"],
    "Maas": [4500, 4800, 5000],
    "Calisma Saati": [40, 38, 36],
    "Sertifika": ["Acil Yardım Sertifikası", "Yara Bakım Sertifikası", "Yoğun Bakım Sertifikası"]
}

hasta_data = {
    "Ad": ["Ali", "Ayşe", "Mehmet"],
    "Soyad": ["Yılmaz", "Demir", "Kaya"],
    "Hasta No": [1, 2, 3],
    "Dogum Tarihi": ["1980-05-15", "1975-09-20", "1990-12-10"],
    "Hastalik": ["Diyabet", "Kanser", "Astım"],
    "Tedavi": ["İlaç Tedavisi", "Kemoterapi", "İnhaler Tedavi"]
}


personel_df = pd.DataFrame(personel_data)
doktor_df = pd.DataFrame(doktor_data)
hemsire_df = pd.DataFrame(hemsire_data)
hasta_df = pd.DataFrame(hasta_data)


birlesik_df = pd.concat([personel_df, doktor_df, hemsire_df, hasta_df])


birlesik_df.reset_index(drop=True, inplace=True)

birlesik_df = birlesik_df.fillna(0)

print("\n\n")

print(birlesik_df)

print("\n\n")

def uzmanlik_gruplandir(df):
    # Group instances of the Doktor class by 'uzmanlik' variable
    gruplandirilmis_df = df.groupby('Uzmanlik')
    
    # Iterate over each group and print their respective counts
    for uzmanlik, grup in gruplandirilmis_df:
        count = grup.shape[0]  # Get the number of rows in each group
        if uzmanlik != 0:
            print(f"Uzmanlik: {uzmanlik}, Sayi: {count}")

uzmanlik_gruplandir(birlesik_df)

print("\n\n 5 Yildan uzun deneyimi olan doktorlar: \n")

def deneyim_gruplandir(df):
    
    deneyim_df = df[df['Deneyim Yili'] > 5]
    
    print(deneyim_df)

deneyim_gruplandir(birlesik_df)

print("\n\n 1990'dan sonra dogan hastalar: \n")

dogum_filtrelenmis_satirlar = hasta_df[hasta_df['Dogum Tarihi'] > '1990']
print(dogum_filtrelenmis_satirlar)

print("\n\n Siralanmis hasta dataframe: \n")

siralanmis_df = hasta_df.sort_values(by='Ad')

print(siralanmis_df)

print("\n\n 7000tl ustu maasi olan personeller: \n")

maas_filtrelenmis_satirlar = personel_df[personel_df['Maas'] > 7000]
print(maas_filtrelenmis_satirlar)


