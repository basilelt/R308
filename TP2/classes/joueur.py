from personnage import Personnage


class Joueur:
    def __init__(self, nom:str, nb_perso:int, personnages:list = []):
        if isinstance(nom, str) and isinstance(nb_perso, int):
            self.__nom:str = nom
            self.__nb_perso:int = nb_perso
            self.__personnages:list = personnages
        
        else:
            raise TypeError("Le nom n'est pas un str ou le nombre de personnage max n'est pas un int")


    def __str__(self) -> str:
        return f"Le joueur {self.__nom} a {len(self.__personnages)} sur {self.__nb_perso} personnages"

    # Getters
    # Récupère la liste de personnage
    @property
    def personnages(self) -> list:
        return self.__personnages
    

    # Setters
    # Remplis la liste de personnages
    @personnages.setter
    def personnages(self, personnage) -> None:
        """
        fonction permettant de remplir la liste de personnage d'un joueur

            :param personnage: personnage à ajouter à la liste du joueur
            :type personnage: Personnage, list
            :raises: TypeError
        """
        if isinstance(personnage, Personnage):
            if (len(self.__personnages) < self.__nb_perso) and (personnage not in self.__personnages):
                self.__personnages.append(personnage)
        
        elif isinstance(personnage, list):
            if len(personnage) >= self.__nb_perso and self.__personnages == []:
                self.__personnages = personnage

        else:
            raise TypeError("Le personnage donné ne fait pas parti de la classe Personnage")
        
    
    def personnage(self, selector) -> Personnage:
        """
        fonction permettant de séléctionner une personnage d'une liste d'un joueur

            :param selector: selecteur du personnage
            :type cible: int, str, Personnage
            :return: personnage
            :rtype: Personnage
            :raises: TypeError
        """
        if isinstance(selector, int):
            return self.__personnages[selector - 1]
        
        elif isinstance(selector, str):
            for personnage in self.__personnages:
                if personnage.pseudo == selector:
                    return personnage

        elif isinstance(selector, Personnage):
            for personnage in self.__personnages:
                if personnage == selector:
                    return personnage
        
        else:
            raise TypeError("Le selecteur de personnage donné n'est ni un int, ni un str, ni un Personnage")


    def eliminer(self, selector) -> None:
        """
        fonction permettant de séléctionner une personnage d'une liste d'un joueur puis de l'enlever

            :param selector: selecteur du personnage
            :type cible: int, str, Personnage
            :raises: TypeError
        """
        if isinstance(selector, int):
            self.__personnages.remove(self.__personnages[selector])
        
        elif isinstance(selector, str):
            for personnage in self.__personnages:
                if personnage.pseudo == selector:
                    self.__personnages.remove(personnage)
                    break

        elif isinstance(selector, Personnage):
            for personnage in self.__personnages:
                if personnage == selector:
                    self.__personnages.remove(personnage)
                    break
        
        else:
            raise TypeError("Le selecteur de personnage donné n'est ni un int, ni un str, ni un Personnage")
