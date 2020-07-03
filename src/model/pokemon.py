import json

from src.entity.pokemon import PokemonEntity


class Pokemon():

    def __init__(self):
        with open('data/pokemones.json', 'r') as file:
            self.pokemones = json.load(file)

    def create(self, pokemon: PokemonEntity):
        self.pokemones.append(pokemon.to_dict())

    def update(self, id: int, pokemon: PokemonEntity):
        pokemon.id = id
        for i in range(0, len(self.pokemones)):
            if self.pokemones[i]['id'] == id:
                self.pokemones[i] = pokemon.to_dict()
                print('Updated!')
                break

    def find(self, id: int):
        for pokemon in self.pokemones:
            if pokemon['id'] == id:
                return pokemon
        return None

    def find_all(self, id_trainer: int):
        pokemones = []
        for pokemon in self.pokemones:
            if pokemon['id_trainer'] == id_trainer:
                pokemones.append(pokemon)
        return pokemones

    def delete(self, id: int):
        pokemon = self.find(id)
        if pokemon is not None:
            self.pokemones.remove(pokemon)
            print('The element with id: ' + str(id) + ' was deleted')
        else:
            print('The element with id: ' + str(id) + ' wasn\'t found')

    def show_pokemones(self):
        return self.pokemones

    def save_data(self):
        with open('data/pokemones.json', 'w') as file:
            json.dump(self.pokemones, file)
