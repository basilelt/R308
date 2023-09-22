from personnage import Personnage


# Classe pour les personnages guerriers
class Guerrier(Personnage):
    def __init__(self, pseudo:str, niveau:int = 1):
        super().__init__(pseudo, niveau)
        
        self.pv = niveau * 8 + 4
        self.initiative = niveau * 4 + 6


    # Getters
    # Récupère le niveau
    @property
    def lvl(self) -> int:
        return self.niveau
    

    # Setters
    @lvl.setter
    def lvl(self, new_niveau):
        if isinstance(new_niveau, int):
            self.niveau = new_niveau
            self.pv = new_niveau * 8 + 4
            self.initiative = new_niveau * 4 + 6
        
        else:
            raise TypeError("La nouvelle valeur du niveau n'est pas un int")
        


    def degats(self) -> float:
        return self.niveau * 2
    
    def soigner(self) -> None:
        self.pv = self.niveau * 8 + 4


# Classe pour les personnages mages
class Mage(Personnage):
    def __init__(self, pseudo:str, niveau:int = 1):
        super().__init__(pseudo, niveau)
        
        self.pv = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        
        self.__mana = niveau * 5
    
    
    # Getters
    # Récupère le niveau
    @property
    def lvl(self) -> int:
        return self.niveau

    
    # Setters
    @lvl.setter
    def lvl(self, new_niveau):
        if isinstance(new_niveau, int):
            self.niveau = new_niveau
            self.pv = new_niveau * 5 + 10
            self.initiative = new_niveau * 6 + 4
            self.__mana = new_niveau * 5
        
        else:
            raise TypeError("La nouvelle valeur du niveau n'est pas un int")


    def degats(self) -> float:
        # Tant qu'il a du mana
        if self.__mana >= 4:
            self.__mana -= 4
            return self.niveau + 3
        
        # Lorsque plus de mana
        else:
            return self.niveau
        
    def soigner(self) -> None:
        self.pv = self.niveau * 5 + 10
        self.__mana = self.niveau * 5


