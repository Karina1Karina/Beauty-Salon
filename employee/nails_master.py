from dataclasses import dataclass
from functools import reduce, lru_cache
from person import Person


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
