from abc import ABC

from pokemon.pokemon import Pokemon


class Aquatic(Pokemon, ABC):
    def __init__(self, nom:str, poids:float, nb_nageoire:int):
        if isinstance(nb_nageoire, int):
            Pokemon().__init__(self, nom, poids)
            self.__nb_nageoire = nb_nageoire
        else:
            raise TypeError("Le nombre de nageoire n'est pas un int")

    def __str__(self):
            return Pokemon().__str__(self) + f"ma vitesse est de {self.vitesse()}km/h j'ai {self.__nb_nageoire} nageoires."

    def vitesse(self):
         return self.poids/25 * self.__nb_nageoire