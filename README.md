# PyPuchamonesProject

You should use python 3.5

### Install pakages

~~~
pip install -r requirements.txt
~~~

### Import classes

~~~
from src.controller.entrenador import EntrenadorController
from src.controller.pokemon import PokemonController
from src.entity.entrenador import EntrenadorEntity
from src.entity.pokemon import PokemonEntity
~~~

### Create an Entrenador

~~~
entrenador = EntrenadorEntity(1, 'dekim', True, 12.3, 'gold')
EntrenadorController().create_entrenador(entrenador)
~~~

### Create a Pokemon

~~~
pokemon = PokemonEntity(1, "Pikachu", True, 'electric', 23, 1)
PokemonController().create_pokemon(pokemon)
~~~

### Find an Entrenador

~~~
print(EntrenadorController().find_entrenador(1))
~~~

## Find a Pokemon

~~~
print(PokemonController().find_pokemon(1))
~~~

## Update an Entrenador

~~~
entrenador.name='Lolito'
EntrenadorController().update_entrenador(1, entrenador)
~~~

## Update a Pokemon

~~~
pokemon.name="Raichu"
PokemonController().update_pokemon(1,pokemon)
~~~

## Show all entrenadores

~~~
EntrenadorController().show_data()
~~~

## Show all pokemones

~~~
PokemonController().show_all()
~~~
