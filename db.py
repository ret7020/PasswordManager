import json
import crypt
import logging

class DataBase:
    def __init__(self, password: str, path: str):
        self.path = path
        self.password = password
        db_read = self.read_db()
        if db_read["status"]:
            self.data = db_read["data"]
        else:
            logging.warning("Can't access data, creating empty database object")
            self.create_db()

    def decrypt_scheme(self, data_bin: bytes):
       pass 

    def create_db(self):
        with open(self.path, "wb") as fd:
            fd.write(b"[]")

    def read_db(self):
        try:
            with open(self.path, "rb") as fd:
                data = json.load(fd)
            return {"status": True, "data": data}
        except Exception as e:
            return {"status": False, "data": e}

    def get_entry(self, entry_id: int):
        pass
        
        
