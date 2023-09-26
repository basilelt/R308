from terrestre import Terrestre


class Sportif(Terrestre):
    def __init__(self, nom:str, poids:float, nb_patte:int, taille:float, frequence:float):
        if isinstance(frequence, float):
            super().__init__(nom, poids, nb_patte, taille)
            self.__frequence = frequence
        else:
            raise TypeError("Le fréquence cardiaque n'est pas un float")

    def __str__(self):
        return super().__str__() + f"ma	fréquence cardiaque	est	de {self.__frequence} pulsations à la minute."
