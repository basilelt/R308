from abc import ABC

class Pokemon(ABC):
    def __init__(self, nom:str, poids:float):
        if isinstance(nom, str) and isinstance(poids, float):
            self.__nom = nom
            self.__poids = poids
        else:
            raise TypeError("Le nom n'est pas un str ou le poids n'est pas un float")
    
    def __str__(self):
        return f"Je suis le pokémon	{self.__nom} mon poids est de {self.__poids} kg, "
    
    @property
    def poids(self) -> float:
        return self.__poids
    