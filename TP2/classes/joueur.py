from personnage import Personnage


class Joueur:
    def __init__(self, nom:str, nb_perso:int, personnages:list = []):
        '''
            Initialise les données de la classe Joueur:
                - nom obligatoire
                - une liste de personnages (peut être vide)
        '''
        if isinstance(nom, str) and isinstance(nb_perso, int):
            self.__nom:str = nom
            self.__nb_perso = nb_perso
            self.__personnages = personnages
        
        else:
            raise TypeError("Le nom n'est pas un str ou le nombre de personnage max n'est pas un int")


    def __str__(self) -> str:
        return f"Le joueur {self.__nom} a {len(self.__personnages)} sur {self.__nb_perso} personnages"

    '''Getter'''
    # Récupère la liste de personnage
    @property
    def personnages(self) -> list:
        return self.__personnages
    

    '''Setter'''
    @personnages.setter
    def personnages(self, personnage:Personnage):
        if isinstance(personnage, Personnage):
            self.__personnages.append(personnage)
        else:
            raise TypeError("Le ")

