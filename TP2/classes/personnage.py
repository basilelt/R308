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


    # Récupère la valeur de l'initiative
    def get_initiative(self):
        return self.__initiative
    
    # Récupère la valeur des pv
    def get_pv(self):
        return self.__pv
    
    # Récupère le pseudo
    def get_pseudo(self):
        return self.__pseudo
    
    # Récupère le niveau
    def get_niveau(self):
        return self.__niveau
    

    # Redéfinie le nombre de pv
    def set_pv(self, new_pv:float):
        if isinstance(new_pv, Union(int, float)):
            self.__pv = new_pv
        
        else:
            raise TypeError("La nouvelle valeur des pv n'est pas un int ou un float")
    

    def __attaque(self, cible:'Personnage') -> str:
        '''
            Test si self à une plus grande initiative que la cible
        '''
        # Self frappe la cible
        if self.__initiative > cible.get_initiative():
            # Si l'attaque de self est supérieure ou égale aux pv de la cible, celle-ci meurt
            if self.__niveau >= cible.get_pv():
                cible.set_pv(0)
                return f"{cible.get_pseudo()} a perdu {self.__niveau}pv et est mort"
            
            # Sinon elle contre attaque
            else:
                # La cible se prend les dégats de self
                cible.set_pv(cible.get_pv() - self.__niveau)
                print(f"{cible.get_pseudo()} a perdu {self.__niveau}pv, il a maintenant {cible.get_pv()}pv")
                
                # Si l'attaque de la cible est supérieure ou égale aux pv de self, celui-ci meurt
                if cible.get_niveau() >= self.__pv:
                    self.__pv = 0
                    return f"{self.__pseudo()} a perdu {cible.get_niveau()}pv et est mort"
                
                # Si self survie, on met à jour ses pv
                else:
                    self.__pv = self.__pv - cible.get_niveau()
                    return f"{self.__pseudo()} a perdu {cible.get_niveau()}pv, il a maintenant {self.__pv()}pv"
                 
        # La cible frappe self
        elif self.__initiative < cible.get_initiative():
            # Si l'attaque de la cible est supérieure ou égale aux pv de self, celui-ci meurt
            if cible.get_niveau() >= self.__pv:
                self.__pv = 0
                return f"{self.__pseudo()} a perdu {cible.get_niveau()}pv et est mort"
            
            # Sinon elle contre attaque
            else:
                # Self se prend les dégats de la cible
                self.__pv = self.__pv - cible.get_niveau()
                print(f"{self.__pseudo()} a perdu {cible.get_niveau()}pv, il a maintenant {self.__pv()}pv")
                
                # Si l'attaque de self est supérieure ou égale aux pv de la cible, celle-ci meurt
                if self.__niveau >= cible.get_pv():
                    cible.set_pv(0)
                    return f"{cible.get_pseudo()} a perdu {self.__niveau}pv et est mort"
                
                # Si la cible survie, on met à jour ses pv
                else:
                    cible.set_pv(cible.get_pv() - self.__niveau)
                    return f"{cible.get_pseudo()} a perdu {self.__niveau}pv, il a maintenant {cible.get_pv()}pv"


        # Self et la cible s'attaque mutuellement
        else:
            # Si l'attaque de la cible est supérieure ou égale aux pv de self, celui-ci meurt
            if cible.get_niveau() >= self.__pv:
                self.__pv = 0
                return f"{self.__pseudo()} a perdu {cible.get_niveau()}pv et est mort"
            
            # Si self survie, on met à jour ses pv
            else:
                self.__pv = self.__pv - cible.get_niveau()
                print(f"{self.__pseudo()} a perdu {cible.get_niveau()}pv, il a maintenant {self.__pv()}pv")
            
            # Si l'attaque de self est supérieure ou égale aux pv de la cible, celle-ci meurt
            if self.__niveau >= cible.get_pv():
                cible.set_pv(0)
                return f"{cible.get_pseudo()} a perdu {self.__niveau}pv et est mort"
            
            # Si la cible survie, on met à jour ses pv
            else:
                cible.set_pv(cible.get_pv() - self.__niveau)
                return f"{cible.get_pseudo()} a perdu {self.__niveau}pv, il a maintenant {cible.get_pv()}pv"


    def combat():
        '''
            Met en place
        '''



    def soigner():
