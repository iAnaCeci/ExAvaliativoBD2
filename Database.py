# from typing import Collection
import pymongo # pip install pymongo
from MotoristaDAO import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.db = database
        self.motorista = Motorista(database)

    def create_motorista(self):
        corridas = input("Enter the title: ")
        nota =  input("Enter the autor: ")
        self.motorista_model.create_motorista(corridas,nota)

    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_person_by_id(id)
        if motorista:
            print(f"corridas: {motorista['corridas']}")
            print(f"nota: {motorista['nota']}")

    def update_motorista(self):
        id = input("Enter the id: ")
        corridas = int(input("Enter: "))
        nota = int(input("Enter the new score:"))
        self.motorista_model.update_person(id, corridas,nota)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_person(id)

    def run(self):
        print("Welcome to the Motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)


