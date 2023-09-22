from typing import Union

import special

# Classe pour les personnage d'un MMORPG
class Personnage:
    """
    Classe définissant un personnage.

        .. py:attribute:: pseudo:

            pseudo du personnage, attribut d'instance

        .. py:attribute:: niveau:

            niveau du personnage, attribut d'instance

        .. py:attribute:: pv:

            pv du personnage, attribut d'instance

        .. py:attribute:: initiative:

            initiative du personnage, attribut d'instance.
    """


    def __init__(self, pseudo:str, niveau:int = 1):
        """
        méthode d'instanciation d'un personnage

            :param pseudo: pseudo du personnage
            :type pseudo: str
            
            :param niveau: niveau du personnage
            :type niveau: int
            
            :param pv: pv du personnage
            :type pv: float

            :param initiative: initiative du personnage
            :type initiative: int
        """
        if isinstance(pseudo, str) and isinstance(niveau, int):
            self.__pseudo:str = pseudo
            self.__niveau:int = niveau
            self.__pv:float = niveau
            self.__initiative:int = niveau
        
        else:
            raise TypeError("Le pseudo n'est pas un str ou le niveau n'est pas un int")
    
    def __str__(self) -> str:
        return f'Le personnage "{self.__pseudo}" est au niveau {self.__niveau}, il lui reste {self.__pv}pv et a une initiative de {self.__initiative}'


    # Getters
    # Récupère la valeur de l'initiative
    @property
    def initiative(self) -> int:
        return self.__initiative
    
    # Récupère la valeur des pv
    @property
    def pv(self) -> float:
        return self.__pv
    
    # Récupère le pseudo
    @property
    def pseudo(self) -> str:
        return self.__pseudo
    
    # Récupère le niveau
    @property
    def niveau(self) -> int:
        return self.__niveau
    

    # Setters
    @pv.setter
    def pv(self, new_pv:float):
        """
        fonction permettant de changer les pv d'un personnage

            :param new_pv: nouvelle valeur de pv du personnage
            :type new_pv: float
            :raises: TypeError
        """
        if isinstance(new_pv, Union[int, float]):
            self.__pv = new_pv
        
        else:
            raise TypeError("La nouvelle valeur des pv n'est pas un int ou un float")
        
    @initiative.setter
    def initiative(self, new_initiative):
        """
        fonction permettant de changer l'initiative d'un personnage

            :param new_initiative: nouvelle valeur de l'initiative du personnage
            :type new_initiative: int
            :raises: TypeError
        """
        if isinstance(new_initiative, int):
            self.__initiative = new_initiative
        
        else:
            raise TypeError("La nouvelle valeur de l'initiative n'est pas un int")
        
    @niveau.setter
    def niveau(self, new_niveau):
        """
        fonction permettant de changer l'initiative d'un personnage

            :param new_initiative: nouvelle valeur de l'initiative du personnage
            :type new_initiative: int
            :raises: TypeError
        """
        if isinstance(new_niveau, int):
            self.__niveau = new_niveau
            self.__pv = new_niveau
            self.__initiative = new_niveau
        
        else:
            raise TypeError("La nouvelle valeur du niveau n'est pas un int")

       
    def __attaque(self, cible:'Personnage') -> str:
        # Self frappe la cible
        if self.__initiative > cible.initiative:
            # Si l'attaque de self est supérieure ou égale aux pv de la cible, celle-ci meurt
            if self.degats() >= cible.pv:
                cible.pv = 0
                return f"{cible.pseudo} a perdu {self.degats()}pv et est mort"
            
            # Sinon elle contre attaque
            else:
                # La cible se prend les dégats de self
                cible.pv = cible.pv - self.degats()
                print(f"{cible.pseudo} a perdu {self.degats()}pv, il a maintenant {cible.pv}pv")
                
                # Si l'attaque de la cible est supérieure ou égale aux pv de self, celui-ci meurt
                if cible.degats() >= self.__pv:
                    self.__pv = 0
                    return f"{self.__pseudo} a perdu {cible.degats()}pv et est mort"
                
                # Si self survie, on met à jour ses pv
                else:
                    self.__pv = self.__pv - cible.degats()
                    return f"{self.__pseudo} a perdu {cible.degats()}pv, il a maintenant {self.__pv}pv"
                 
        # La cible frappe self
        elif self.__initiative < cible.initiative:
            # Si l'attaque de la cible est supérieure ou égale aux pv de self, celui-ci meurt
            if cible.degats() >= self.__pv:
                self.__pv = 0
                return f"{self.__pseudo} a perdu {cible.degats()}pv et est mort"
            
            # Sinon elle contre attaque
            else:
                # Self se prend les dégats de la cible
                self.__pv = self.__pv - cible.degats()
                print(f"{self.__pseudo} a perdu {cible.degats()}pv, il a maintenant {self.__pv}pv")
                
                # Si l'attaque de self est supérieure ou égale aux pv de la cible, celle-ci meurt
                if self.degats() >= cible.pv:
                    cible.pv = 0
                    return f"{cible.pseudo} a perdu {self.degats()}pv et est mort"
                
                # Si la cible survie, on met à jour ses pv
                else:
                    cible.pv = cible.pv - self.degats()
                    return f"{cible.pseudo} a perdu {self.degats()}pv, il a maintenant {cible.pv}pv"


        # Self et la cible s'attaque mutuellement
        else:
            # Si l'attaque de la cible est supérieure ou égale aux pv de self, celui-ci meurt
            if cible.degats() >= self.__pv:
                self.__pv = 0
                return f"{self.__pseudo} a perdu {cible.degats()}pv et est mort"
            
            # Si self survie, on met à jour ses pv
            else:
                self.__pv = self.__pv - cible.degats()
                print(f"{self.__pseudo} a perdu {cible.degats()}pv, il a maintenant {self.__pv}pv")
            
            # Si l'attaque de self est supérieure ou égale aux pv de la cible, celle-ci meurt
            if self.degats() >= cible.pv:
                cible.pv = 0
                return f"{cible.pseudo} a perdu {self.degats()}pv et est mort"
            
            # Si la cible survie, on met à jour ses pv
            else:
                cible.pv = cible.pv - self.degats()
                return f"{cible.pseudo} a perdu {self.degats()}pv, il a maintenant {cible.pv}pv"


    def combat(self, cible:'Personnage') -> str:
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
        self.__pv = self.__niveau
    

    def degats(self) -> float:
        return self.niveau
