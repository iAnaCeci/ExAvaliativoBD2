from pymongo import MongoClient
from bson.objectid import ObjectId

from Model.Corrida import Corrida
from Model.Motorista import Motorista


class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista:Motorista):
        try:
            res = self.db.collection.insert_one({ "corridas":[{"nota":motorista.corridas.nota,"distancia":motorista.corridas.distancia, "valor":motorista.corridas.valor,"passageiro":{
                "nome":motorista.corridas.passageiro.nome,
                "documento":motorista.corridas.passageiro.documento
            }}],"nota":motorista.notas})
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

