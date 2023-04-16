from pymongo import MongoClient
from bson.objectid import ObjectId

class Motorista:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, corridas:str, nota: int):
        try:
            res = self.db.collection.insert_one({ "corridas":corridas,"nota":nota})
            print(f"Motorista created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motoristafound: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, id: str, corridas:str, nota: int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"corridas":corridas,"nota":nota}})
            print(f"Motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None

class Corrida:
    def __init__(self, database):
        self.db = database
        self.collection = self.db.corridas

    def create_corrida(self, nota: float, distancia: float, valor: float, passageiro: dict):
        corrida = {
            "nota": nota,
            "distancia": distancia,
            "valor": valor,
            "passageiro": passageiro
        }
        try:
            res = self.collection.insert_one(corrida)
            print(f"Corrida created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating corrida: {e}")
            return None

    def read_corrida_by_id(self, id: str):
        try:
            res = self.collection.find_one({"_id": ObjectId(id)})
            print(f"Corrida found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading corrida: {e}")
            return None

    def update_corrida(self, id: str, nota: float, distancia: float, valor: float, passageiro: dict):
        corrida = {
            "nota": nota,
            "distancia": distancia,
            "valor": valor,
            "passageiro": passageiro
        }
        try:
            res = self.collection.update_one({"_id": ObjectId(id)}, {"$set": corrida})
            print(f"Corrida updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating corrida: {e}")
            return None

    def delete_corrida(self, id: str):
        try:
            res = self.collection.delete_one({"_id": ObjectId(id)})
            print(f"Corrida deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting corrida: {e}")
            return None

class Passageiro:
    def __init__(self, database):
        self.db = database
        self.collection = self.db.passageiros

    def create_passageiro(self, nome: str, documento: str):
        passageiro = {
            "nome": nome,
            "documento": documento
        }
        try:
            res = self.collection.insert_one(passageiro)
            print(f"Passageiro created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating passageiro: {e}")
            return None

    def read_passageiro_by_id(self, id: str):
        try:
            res = self.collection.find_one({"_id": ObjectId(id)})
            print(f"Passageiro found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading passageiro: {e}")
            return None

    def update_passageiro(self, id: str, nome: str, documento: str):
        passageiro = {
            "nome": nome,
            "documento": documento
        }
        try:
            res = self.collection.update_one({"_id": ObjectId(id)}, {"$set": passageiro})
            print(f"Passageiro updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating passageiro: {e}")

