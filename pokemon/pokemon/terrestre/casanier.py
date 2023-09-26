from pokemon.terrestre.terrestre import Terrestre
from datetime import time


class Casanier(Terrestre):
    def __init__(self, nom:str, poids:float, nb_patte:int, taille:float, heure:time):
        if isinstance(heure, time):
            super().__init__(nom, poids, nb_patte, taille)
            self.__heure = heure
        else:
            raise TypeError("L'heure n'est pas de type time")

    def __str__(self):
        return super().__str__() + f"je regarde la télé {self.__heure} par jour."
