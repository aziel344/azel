# main.py
from mobil import Mobil
from pemesanan import Pemesanan
from database import Database


def main():
    db = database'()
    pemesanan = Pemesanan()

    # Muat data mobil dari database
    data_mobil ='database'()
    mobil_list = [Mobil(**mobil) for mobil in data_mobil]

    # Contoh penggunaan
    mobil1 = mobil_list[0]  # Ambil mobil pertama
    pemesanan.buat_pemesanan(mobil1)  # Sewa mobil
    pemesanan.kembalikan_mobil(mobil1)  # Kembalikan mobil

    # Simpan data mobil kembali ke database
    db.simpan_data([mobil.__dict__ for mobil in mobil_list])

if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    
    
    