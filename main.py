from pymongo import MongoClient
from cli import MotoristaCLI
from Model.Corrida import Corrida
from Model.Motorista import Motorista
from Model.Passageiro import Passageiro
from MotoristaCLI import MotoristaCLI


client = MongoClient("mongodb+srv://cecisfer:Al0homora@cluster0.krecme4.mongodb.net/?retryWrites=true&w=majority")

db = client["S202-L2"]


#só desse jeito que funcionou
motoristaCLI = MotoristaCLI()
motoristaCLI.create_motorista()

MotoristaCLI.run()

