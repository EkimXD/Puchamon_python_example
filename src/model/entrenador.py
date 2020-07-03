import json

from src.entity.entrenador import EntrenadorEntity


class Entrenador():

    def __init__(self):
        with open('data/entrenadores.json', 'r') as file:
            self.entrenadores = json.load(file)

    def create(self, entrenador: EntrenadorEntity):
        self.entrenadores.append(entrenador.to_dict())

    def update(self, id: int, entrenador: EntrenadorEntity):
        entrenador.id = id
        for i in range(0, len(self.entrenadores)):
            if self.entrenadores[i]['id'] == id:
                self.entrenadores[i] = entrenador.to_dict()
                print('Updated!')
                break

    def find(self, id: int):
        for entrenador in self.entrenadores:
            if entrenador['id'] == id:
                return entrenador
        return None

    def delete(self, id: int):
        entrenador = self.find(id)
        if entrenador is not None:
            self.entrenadores.remove(entrenador)
            print('The element with id: ' + str(id) + ' was deleted')
        else:
            print('The element with id: ' + str(id) + ' wasn\'t found')

    def show_entrenadores(self):
        return self.entrenadores

    def save_data(self):
        with open('data/entrenadores.json', 'w') as file:
            json.dump(self.entrenadores, file)
