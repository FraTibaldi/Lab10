from database.DB_connect import DBConnect
from model.filiale import Filiale

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    def __init__(self):
        pass

    @staticmethod
    def read_filiali():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT * FROM filiale")
                result = {}
                for row in cursor:
                    filiale = Filiale(**row)
                    result[filiale.id] = filiale
                return result
            finally:
                cursor.close()
        finally:
            conn.close()

    @staticmethod
    def read_collegamenti_pesati():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """SELECT LEAST(id_filiale_origine, id_filiale_destinazione) AS filiale1,
                                  GREATEST(id_filiale_origine, id_filiale_destinazione) AS filiale2,
                                  AVG(importo) AS peso
                           FROM bonifico
                           GROUP BY filiale1, filiale2"""
                cursor.execute(query)
                result = {}
                for row in cursor:
                    result[(row["filiale1"], row["filiale2"])] = row["peso"]
                return result
            finally:
                cursor.close()
        finally:
            conn.close()
