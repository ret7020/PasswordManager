from db import DataBase
import logging

logging.basicConfig(level=logging.INFO, filename="runtime.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")


if __name__ == "__main__":
    password = "123456789"
    db = DataBase(password, "./base")
