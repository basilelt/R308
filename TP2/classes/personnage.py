from typing import Union


# Classe pour les personnage d'un MMORPG
class Personnage:
    def __init__(self, pseudo:str, niveau:int = 1):
        '''
            Initialise les données de la classe Personnage:
                - pseudo obligatoire
                - niveau de base à 1
                - pv et initiative prennent la valeur du niveau
        '''
        if isinstance(pseudo, str) and isinstance(niveau, int):
            pv:float = niveau
            initiative:int = niveau
        
            self.__pseudo:str = pseudo
            self.__niveau:int = niveau
            self.__pv:float = pv
            self.__initiative:int = initiative
        
        else:
            raise TypeError("Le pseudo n'est pas un str ou le niveau n'est pas un int")
    
    def __str__(self) -> str:
        '''
            Retourne les informations d'un personnage
        '''
        return f'Le personnage "{self.__pseudo}" est au niveau {self.__niveau}, il lui reste {self.__pv} et a une initiative de {self.__initiative}'


    '''Getter'''
    # Récupère la valeur de l'initiative
    @property
    def initiative(self):
        return self.__initiative
    
    # Récupère la valeur des pv
    @property
    def pv(self):
        return self.__pv
    
    # Récupère le pseudo
    @property
    def pseudo(self):
        return self.__pseudo
    
    # Récupère le niveau
    @property
    def niveau(self):
        return self.__niveau
    

    ''' Setter '''
    # Redéfinie le nombre de pv
    @pv.setter
    def pv(self, new_pv:float):
        if isinstance(new_pv, Union[int, float]):
            self.__pv = new_pv
        
        else:
            raise TypeError("La nouvelle valeur des pv n'est pas un int ou un float")
        
    # Redéfinie l'initiative
    @initiative.setter
    def initiative(self, new_initiative):
        if isinstance(new_initiative, int):
            self.__initiative = new_initiative
        
        else:
            raise TypeError("La nouvelle valeur de l'initiative n'est pas un int")
    

    def __attaque(self, cible:'Personnage') -> str:
        '''
            Test si self à une plus grande initiative que la cible
        '''
        # Self frappe la cible
        if self.__initiative > cible.initiative:
            # Si l'attaque de self est supérieure ou égale aux pv de la cible, celle-ci meurt
            if self.__niveau >= cible.pv:
                cible.pv = 0
                return f"{cible.pseudo} a perdu {self.__niveau}pv et est mort"
            
            # Sinon elle contre attaque
            else:
                # La cible se prend les dégats de self
                cible.pv = cible.pv - self.__niveau
                print(f"{cible.pseudo} a perdu {self.__niveau}pv, il a maintenant {cible.pv}pv")
                
                # Si l'attaque de la cible est supérieure ou égale aux pv de self, celui-ci meurt
                if cible.niveau >= self.__pv:
                    self.__pv = 0
                    return f"{self.__pseudo} a perdu {cible.niveau}pv et est mort"
                
                # Si self survie, on met à jour ses pv
                else:
                    self.__pv = self.__pv - cible.niveau
                    return f"{self.__pseudo} a perdu {cible.niveau}pv, il a maintenant {self.__pv}pv"
                 
        # La cible frappe self
        elif self.__initiative < cible.initiative:
            # Si l'attaque de la cible est supérieure ou égale aux pv de self, celui-ci meurt
            if cible.niveau >= self.__pv:
                self.__pv = 0
                return f"{self.__pseudo} a perdu {cible.niveau}pv et est mort"
            
            # Sinon elle contre attaque
            else:
                # Self se prend les dégats de la cible
                self.__pv = self.__pv - cible.niveau
                print(f"{self.__pseudo} a perdu {cible.niveau}pv, il a maintenant {self.__pv}pv")
                
                # Si l'attaque de self est supérieure ou égale aux pv de la cible, celle-ci meurt
                if self.__niveau >= cible.pv:
                    cible.pv = 0
                    return f"{cible.pseudo} a perdu {self.__niveau}pv et est mort"
                
                # Si la cible survie, on met à jour ses pv
                else:
                    cible.pv = cible.pv - self.__niveau
                    return f"{cible.pseudo} a perdu {self.__niveau}pv, il a maintenant {cible.pv}pv"


        # Self et la cible s'attaque mutuellement
        else:
            # Si l'attaque de la cible est supérieure ou égale aux pv de self, celui-ci meurt
            if cible.niveau >= self.__pv:
                self.__pv = 0
                return f"{self.__pseudo} a perdu {cible.niveau}pv et est mort"
            
            # Si self survie, on met à jour ses pv
            else:
                self.__pv = self.__pv - cible.niveau
                print(f"{self.__pseudo} a perdu {cible.niveau}pv, il a maintenant {self.__pv}pv")
            
            # Si l'attaque de self est supérieure ou égale aux pv de la cible, celle-ci meurt
            if self.__niveau >= cible.pv:
                cible.pv = 0
                return f"{cible.pseudo} a perdu {self.__niveau}pv et est mort"
            
            # Si la cible survie, on met à jour ses pv
            else:
                cible.pv = cible.pv - self.__niveau
                return f"{cible.pseudo} a perdu {self.__niveau}pv, il a maintenant {cible.pv}pv"


    def combat(self, cible:'Personnage') -> str:
        '''
            Met en place les attaques jusqu'à ce que mort s'en suive
        '''
        # Tant que les deux personnages ont encore de la vie le combat continue
        while self.__pv > 0 and cible.pv > 0:
            print(self.__attaque(cible))
        
        if self.__pv == 0 and cible.pv == 0:
            self.soigner()
            cible.soigner()
            return f"{self.__pseudo} et {cible.pseudo} sont tous les deux morts, égalité"
        
        elif self.__pv == 0:
            self.soigner()
            return f"{cible.pseudo} a gagné"
        
        else:
            cible.soigner()
            return f"{self.__pseudo} a gagné"


    def soigner(self) -> None:
        '''
            Soigne les pv de self et les met à la valeur de son niveau
        '''
        self.__pv = self.__niveau
