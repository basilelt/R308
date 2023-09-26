from abc import ABC
from sys import path


# Ajoute le dossier classes au path
path.insert(0, __file__.replace("terrestre/terrestre.py", ""))

from pokemon.pokemon import Pokemon


class Terrestre(Pokemon, ABC):
    def __init__(self, nom:str, poids:float, nb_patte:int, taille:float):
        if isinstance(nb_patte, int) and isinstance(taille, float):
            Pokemon().__init__(self, nom, poids)
            self.__nb_patte = nb_patte
            self.__taille = taille
        else:
            raise TypeError("Le nombre de pattes n'est pas un int ou la taille n'est pas un float")

    def __str__(self):
        return Pokemon().__str__(self) + f"ma vitesse	est de {self.vitesse()}km/h	j'ai {self.__nb_patte} pattes, ma taille est de	{self.__taille}m "
    
    def vitesse(self):
        return self.__nb_patte * self.__taille * 3
