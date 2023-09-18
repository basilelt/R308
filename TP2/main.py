from sys import exit, path
from os import path as ospath

# Ajoute le dossier classes au path
path.insert(0, ospath.join(__file__.replace("main.py", ""), "classes"))

from classes.personnage import Personnage
from classes.special import Mage, Guerrier


def main():
    player1 = Personnage("player1", 2)
    player2 = Personnage("player2", 5)
    print(f"\n{player1.combat(player2)}\n")
    
    player3 = Personnage("player3")
    player4 = Personnage("player4")
    print(f"\n{player3.combat(player4)}\n")

    mage1 = Mage("mage1")
    guerrier1 = Guerrier("guerrier1")
    print(f"\n{mage1.combat(guerrier1)}\n")

    mage2 = Mage("mage2", 3)
    guerrier2 = Guerrier("guerrier2", 2)
    print(f"\n{mage2.combat(guerrier2)}\n")


if __name__ == "__main__":
    '''
        Exécute la fonction main si le nom du fichier exécuté est main.py
    '''
    exit(main())