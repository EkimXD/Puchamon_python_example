from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class EntrenadorEntity:
    id: int
    name: str
    active: bool
    distance: float
    level: str
    pokemon = []
