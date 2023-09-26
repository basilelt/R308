from aquatic import Aquatic


class Croisiere(Aquatic):
    def __init__(self, nom:str, poids:float, nb_nageoire:int):
        if isinstance(nb_nageoire, int):
            super().__init__(nom, poids)
            self.__nb_nageoire = nb_nageoire
        else:
            raise TypeError("Le nombre de nageoires n'est pas un int")

    def __str__(self):
        return super().__str__() + f"j'ai {self.__nb_nageoire} nageoires."
    
    def vitesse(self):
        return super().vitesse()/2
