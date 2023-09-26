from sys import exit, path
from os import path as ospath

# Ajoute le dossier classes au path
path.insert(0, ospath.join(__file__.replace("main.py", ""), "pokemon"))


from pokemon.terrestre.sportif import Sportif
from pokemon.terrestre.casanier import Casanier
from pokemon.aquatic.mer import Mer
from pokemon.aquatic.croisiere import Croisiere


def main():
    poke_pikachu = Sportif("Pikachu", 18, 2, 0.85, 120)
    print(poke_pikachu)


if __name__ == "__main__":
    exit(main())
