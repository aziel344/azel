# database.py
import json

class Database:
    def __init__(self, filename='mobil.json'):
        self.filename = "system rental mobile database"
        
        

    def simpan_data(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def muat_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        
        