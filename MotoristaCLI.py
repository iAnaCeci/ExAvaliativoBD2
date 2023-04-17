from Model.Corrida import Corrida
from Model.Motorista import Motorista
from Model.Passageiro import Passageiro
from MotoristaDAO import MotoristaDAO
from Database import Database

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self):
        super().__init__()
        self.add_command("create",self.create_motorista())
        self.add_command("read",self.read_motorista())
        self.add_command("update",self.update_motorista())
        self.add_command("delete",self.delete_motorista())

    def create_motorista(self):
        nota = int(input("Entre com a nota"))
        nota_corrida = int(input("Entre com a nota da corrida"))
        distancia = float(input("Entre com a distancia"))
        valor = float(input("Entre com o valor"))
        passageiro_nome = input("Nome do passageiro")
        passageiro_documento = input("Documento do passageiro")
        passageiro = Passageiro(passageiro_nome,passageiro_documento)
        corrida = Corrida(nota_corrida,distancia,valor,passageiro)
        motorista = Motorista(corrida,nota)
        con_banco = MotoristaDAO(Database("ExAvaliativoAtlas","motorista"))
        con_banco.create_motorista(motorista)

    def read_motorista(self, motorista=None):
        # def read_motorista(self):
        #     motorista_id = int(input("Enter the ID of the motorista you want to read: "))
        #     con_banco = MotoristaDAO(Database("ExAvaliativoAtlas", "motorista"))
        #     motorista = con_banco.read_motorista(motorista_id)
        #     if motorista:
        #         print("Motorista found!")
        #         print(motorista)
        #     else:
        #         print("Motorista not found.")
        pass
    def update_motorista(self):
        # motorista_id = int(input("Enter the ID of the motorista you want to update: "))
        # con_banco = MotoristaDAO(Database("ExAvaliativoAtlas", "motorista"))
        # motorista = con_banco.read_motorista(motorista_id)
        # if motorista:
        #     print("Motorista encontrado!")
        #     nota = int(input("Enter the new nota: "))
        #     nota_corrida = int(input("Enter the new nota da corrida: "))
        #     distancia = float(input("Enter the new distancia: "))
        #     valor = float(input("Enter the new valor: "))
        #     motorista.nota = nota
        #     motorista.corrida.nota = nota_corrida
        #     motorista.corrida.distancia = distancia
        #     motorista.corrida.valor = valor
        #     con_banco.update_motorista(motorista)
        #     print("Motorista atualizado!")
        # else:
        #     print("Motorista not found.")
        pass

    def delete_motorista(self):
        # motorista_id = int(input("Enter the ID of the motorista you want to delete: "))
        # con_banco = MotoristaDAO(Database("ExAvaliativoAtlas", "motorista"))
        # motorista = con_banco.read_motorista(motorista_id)
        # if motorista:
        #     print("Motorista encontrado!")
        #     con_banco.delete_motorista(motorista)
        #     print("Motorista deletado!")
        # else:
        #     print("Motorista nao encontrado.")
        pass

    def run(self):
        print("Welcome to the Motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()