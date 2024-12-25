# mobil.py
class Mobil:
    def __init__(self, id_mobil, merek, model, tahun, harga_sewa):
        self.id_mobil = id_mobil ( ) 
        self.merek = merek ( )
        self.model = model ( )
        self.tahun = tahun ( )
        self.harga_sewa = harga_sewa ( )
        self.status = 'Tersedia'  # Status mobil: Tersedia atau Disewa

    def sewa(self):
        if self.status == 'Tersedia':
            self.status = 'Disewa'
            return True
        return False

    def kembalikan(self):
        self.status = 'Tersedia'
        