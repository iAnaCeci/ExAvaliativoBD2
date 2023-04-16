from pymongo import MongoClient

from cli import MotoristaCLI
from MotoristaDAO import Motorista
from MotoristaDAO import Corrida
from MotoristaDAO import Passageiro

client = MongoClient("mongodb://localhost:27017/")

db = client["ExAvaliativo"]
motoristaCLI = MotoristaCLI(database=db)


motorista = Motorista(db)
corrida = Corrida(db)
passageiro = Passageiro(db)


motoristaCLI.run()