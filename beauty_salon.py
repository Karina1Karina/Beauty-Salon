from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Person(ABC):
    name: str

    @abstractmethod
    def get_info(self):
        raise NotImplemented
