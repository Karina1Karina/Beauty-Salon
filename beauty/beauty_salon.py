import imp
from ..employee.beautician import Beautician
from ..employee.nails_master import NailsMaster


class BeautySalon:
    count_clients = 0
    suma = 0

    def __init__(self):
        BeautySalon.count_clients +=1
        BeautySalon.suma = 0
    
    @classmethod
    def return_count(cls):
        return f"Count of beauty salon clients: {cls.count_clients}"
    
    @staticmethod
    def description():
        return "This salon provides the following services: manicure, makeup."

    def makeup_procedure(self, makeup: Beautician):
        BeautySalon.suma += makeup.do_makeup()

    def manicure_procedure(self, manicure: NailsMaster):
        BeautySalon.suma += manicure.do_manicure()
    
    def cost(self):
        return f"Final cost: {BeautySalon.suma}$"