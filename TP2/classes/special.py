from personnage import Personnage


# Classe pour les personnages guerriers
class Guerrier(Personnage):
    '''
        Initialise les valeurs de pv et initiative propres à la classe Guerrier
    '''
    def __init__(self, pseudo:str, niveau:int = 1):
        super().__init__(pseudo, niveau)
        
        self.pv = niveau * 8 + 4
        self.initiative = niveau * 4 + 6


# Classe pour les personnages mages
class Mage(Personnage):
    '''
        Initialise les valeurs de pv, initiative et mana propres à la classe Mage
    '''
    def __init__(self, pseudo:str, niveau:int = 1):
        super().__init__(pseudo, niveau)
        
        self.pv = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        
        self.__mana = niveau * 5