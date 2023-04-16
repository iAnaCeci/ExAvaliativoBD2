from MotoristaDAO import Motorista, Corrida, Passageiro
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
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas = input("Enter the title: ")
        nota =  input("Enter the autor: ")
        nome = input("Enter the passenger name: ")
        documento = input("Enter the passenger document: ")
        self.motorista_model.create_person(corridas, nota)
        passageiro = Passageiro(nome, documento)
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
        self.motorista.delete_person(id)

    def run(self):
        print("Welcome to the Motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()