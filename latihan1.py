# Atribut Class
class Siswa:
    sekolah = "SMK PGRI 35 Solokanjeruk"

    # Konstruktor
    def __init__(self, nama, nis, kelas):
        self.nama = nama
        self.nis = nis
        self.kelas = kelas

    # Method
    def tampilkan_profil_siswa(self):
        print(f"Nama    : {self.nama}")
        print(f"NIS     : {self.nis}")
        print(f"Kelas   : {self.kelas}")
        print(f"Sekolah : {Siswa.sekolah}")


# Membuat Objek
s1 = Siswa("Deden Supriatna", "12345", "XI RPL 3")

# Memanggil Method
s1.tampilkan_profil_siswa()