from abc import ABC
from typing import Union
from pokemon.pokemon import Pokemon


class Terrestre(Pokemon, ABC):
    def __init__(self, nom:str, poids:float, taille:float, nb_patte:int):
        if isinstance(nb_patte, int) and isinstance(taille, Union[int, float]):
            Pokemon().__init__(self, nom, poids)
            self.__nb_patte = nb_patte
            self.__taille = taille
        else:
            raise TypeError("Le nombre de pattes n'est pas un int ou la taille n'est pas un float")

    def __str__(self):
        return Pokemon().__str__(self) + f"ma vitesse	est de {self.vitesse()}km/h	j'ai {self.__nb_patte} pattes, ma taille est de	{self.__taille}m "
    
    def vitesse(self):
        return self.__nb_patte * self.__taille * 3
