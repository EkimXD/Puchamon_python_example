from src.model.pokemon import Pokemon
from src.entity.pokemon import PokemonEntity


class PokemonController():

    def __init__(self):
        self.pokemones = Pokemon()

    def create_pokemon(self, pokemon: PokemonEntity):
        self.pokemones.create(pokemon)
        self.pokemones.save_data()  # if you want you can remove this line!

    def find_pokemon(self, id: int):
        return self.pokemones.find(id)

    def delete_pokemon(self, id: int):
        self.pokemones.delete(id)
        self.pokemones.save_data()  # if you want you can remove this line!

    def update_pokemon(self, id: int, pokemon: PokemonEntity):
        self.pokemones.update(id, pokemon)
        self.pokemones.save_data()  # if you want you can remove this line!

    def show_all(self):
        print(self.pokemones.show_pokemones())