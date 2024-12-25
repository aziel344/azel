# pemesanan.py
from mobil import Mobil

class Pemesanan:
    def __init__(self):
        self.pemesanan_list = []

    def buat_pemesanan(self, mobil):
        if mobil.sewa():
            self.pemesanan_list.append(mobil)
            print(f'Mobil {mobil.merek} {mobil.model} berhasil disewa.')
        else:
            print(f'Mobil {mobil.merek} {mobil.model} tidak tersedia.')

    def kembalikan_mobil(self, mobil):
        mobil.kembalikan()
        self.pemesanan_list.remove(mobil)
        print(f'Mobil {mobil.merek} {mobil.model} berhasil dikembalikan.')
        