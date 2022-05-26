from dataclasses import dataclass
from functools import reduce
from person import Person


@dataclass
class Beautician(Person):
    price = 0

    def get_info(self):
        return "Person that doing makeup"

    def do_makeup(self):
        process_of_makeup = {"Foundation": 180, "Eyebrows": 100, "Eyes":150, "Lips": 80}
        self.price = reduce(lambda x, y: x + y, process_of_makeup.values())
        return self.price
    
    def __str__(self):
        return f"Beautician with name -> {self.name}"

    def __eq__(self, other):
        return self.name == other.name
    
    def __add__(self, other):
        return self.price + other.price
    
    def __copy__(self):
        return Beautician(self.name)
