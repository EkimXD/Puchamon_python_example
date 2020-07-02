from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PokemonEntity:
    id: int
    name: str
    active: bool
    level: str
    id_trainer: int
