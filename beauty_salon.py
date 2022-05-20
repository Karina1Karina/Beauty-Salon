from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import reduce, lru_cache


@dataclass
class Person(ABC):
    name: str

    @abstractmethod
    def get_info(self):
        raise NotImplemented


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


@dataclass
class NailsMaster(Person):

    def get_info(self):
        return "Person that doing manicure"
    

    @lru_cache
    def do_manicure(self):
        process_of_manicure = {"Correction": 100, "Nail extension": 200, "Gel coating": 150}
        price = reduce(lambda x, y: x + y, process_of_manicure.values())
        return price


    def __str__(self):
        return f"Nails Master with name -> {self.name}"
