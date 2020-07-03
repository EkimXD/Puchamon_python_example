from src.model.entrenador import Entrenador
from src.model.pokemon import Pokemon
from src.entity.entrenador import EntrenadorEntity


class EntrenadorController():

    def __init__(self):
        self.entrenadores = Entrenador()
        self.pokemones = Pokemon()

    def create_entrenador(self, entrenador: EntrenadorEntity):
        self.entrenadores.create(entrenador)
        self.entrenadores.save_data()  # if you want you can remove this line!

    def find_entrenador(self, id: int):
        entrenador = self.entrenadores.find(id)
        if entrenador is not None:
            entrenador['pokemon'] = self.pokemones.find_all(entrenador['id'])
        return entrenador

    def delete_entrenador(self, id: int):
        self.entrenadores.delete(id)
        self.entrenadores.save_data()  # if you want you can remove this line!

    def update_entrenador(self, id: int, entrenador: EntrenadorEntity):
        self.entrenadores.update(id, entrenador)
        self.entrenadores.save_data()  # if you want you can remove this line!

    def show_data(self):
        print(self.entrenadores.show_entrenadores())