from Model.Corrida import Corrida


class Motorista:
    def __init__(self, corrida:Corrida,notas:int):
        self.corridas = corrida
        self.notas = notas