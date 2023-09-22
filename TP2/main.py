from sys import exit, path
from os import path as ospath

# Ajoute le dossier classes au path
path.insert(0, ospath.join(__file__.replace("main.py", ""), "classes"))

from classes.personnage import Personnage
from classes.special import Mage, Guerrier
from classes.joueur import Joueur


def main():
    mob1 = Personnage("mob1", 2)
    mob2 = Personnage("mob2", 5)
    print(mob2)
    print(f"\n{mob1.combat(mob2)}\n")
    print(mob2)
    
    mob3 = Personnage("mob3")
    mob4 = Personnage("mob4")
    print(f"\n{mob3.combat(mob4)}\n")

    mage1 = Mage("mage1")
    guerrier1 = Guerrier("guerrier1")
    print(f"\n{mage1.combat(guerrier1)}\n")

    mage2 = Mage("mage2", 3)
    guerrier2 = Guerrier("guerrier2", 2)
    print(f"\n{mage2.combat(guerrier2)}\n")


    player1 = Joueur("player1", 3)
    player2 = Joueur("player2", 5, [mob1, mage1, guerrier1])
    print(player2)

    print(f"\n{print(mage1)}")
    mage1.lvl = 10
    print(mage1)


if __name__ == "__main__":
    exit(main())