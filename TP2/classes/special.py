from personnage import Personnage


# Classe pour les personnages guerriers
class Guerrier(Personnage):
    def __init__(self, pseudo:str, niveau:int = 1):
        super().__init__(pseudo, niveau)
        
        self.pv = niveau * 8 + 4
        self.initiative = niveau * 4 + 6


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