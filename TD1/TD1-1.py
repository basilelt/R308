def test_bool(to_bool):
    while True:
        test = True
        try:
            to_bool = int(to_bool)
        except ValueError:
            to_bool = input("Désolé la valeur saisie n'est pas un nombre, réessayez: ")
            test = False
            
        if test:
            if to_bool == 0 or to_bool == 1:
                bool(to_bool)
                return to_bool
            
            else:
                to_bool = input("Veuillez entrer une valeur étant 0 (Non) ou 1 (Oui), réessayez: ")

def test_selector(to_selector):
    while True:
        test = False
        try:
            to_selector = int(to_selector)
            test = True
        except ValueError:
            to_selector = input("Désolé la valeur saisie n'est pas un int, réessayez: ")
        
        if test:
            if to_selector in [1, 2, 3, 4, 5]:
                return to_selector
            else:
                to_selector = input("Veuillez choisir un nombre de la liste (entre 1 et 5): ")

def test_int(to_int):
    while True:
        try:
            to_int = int(to_int)
            return to_int
        except ValueError:
            to_int = input("Désolé la valeur saisie n'est pas un int, réessayez: ")

def test_float(to_float):
    while True:
        try:
            to_float = float(to_float)
            return to_float
        except ValueError:
            to_float = input("Désolé la valeur saisie n'est pas un float, réessayez: ")


#1
def maximum(x:float, y:float) -> float:
    """
        Fonction qui retourne le plus grand de deux nombres réels.
    """
    return max(x, y)

#2
def superieur(x:float, ceil = 10) -> bool:
    """
        Fonction qui indique si la valeur passée est supérieure à un seuil.
    """
    if x > ceil:
        return True
    else:
        return False

#3    
def max_list(lst:list) -> float:
    """
        Fonction qui retourne la plus grande valeur d'une liste fournit.
    """
    return(max(lst))

#4
def inf_list(lst:list) -> int:
    """
        Fonction qui retourne le nombre de valeurs d'une liste inférieures à un seuil.
    """
    ceil = 3
    count = 0
    list_choice = test_bool(
                input("Voulez-vous choisir le seuil ?\n"
                      "Oui: 1 / Non: 0 : ")
                )
    if list_choice:
        ceil = input("Quel seuil voulez-vous: ")
    
    for i in lst:
        if i < ceil:
            count += 1
    
    return count
    

#5    
def dictionnaire(dico:dict, cara:str):
    """
        Fonction qui affiche l'ensemble des données d'un dictionnaire.
    """
    for key, value in dico.items():
        print(cara, " ", key, " ", value)


# Choix de la fonction à exécuter
choice = test_selector(
            input("Sélectionnez la fonction à exécuter:\n"
                  "Maximum: 1\n"
                  "Supérieur: 2\n"
                  "Maximum Liste: 3\n"
                  "Inférieur Liste: 4\n"
                  "Dictionnaire: 5\n"
                  " -> ")
            )

if choice == 1:
    print("Retourne le plus grand nombre de deux réels.")
    print(maximum(
            test_float(input('Entrez le 1er nombre: ')),
            test_float(input('Entrez le 2ème nombre: ')))
        )

elif choice == 2:
    print("Indique si la valeur est supérieure à un seuil.")
    x = input("Veuillez choisir un nombre: ")
    ceil_choice = test_bool(
                    input("Voulez-vous choisir le seuil ?\n"
                          "Oui: 1 / Non: 0 : ")
                )
    if ceil_choice:
        print(superieur(x, input("Entrez le seuil: ")))
    else:
         superieur(x)

elif choice == 3:
    print("La plus grande valeur d'une liste.")
    stop = False
    lst=[]
    while stop is False:
        lst.append(input("Entrez un nouveau nombre (x pour arrêter): "))
        if lst[-1] == "x":
            stop = True
            lst.pop()
    
    print(f"{max_list(lst)} est le maximum.")


elif choice == 4:
    print("Le nombre de valeurs d'une liste inférieure à un seuil.")
    stop = False
    lst=[]
    while stop is False:
        lst.append(input("Entrez un nouveau nombre (x pour arrêter): "))
        if lst[-1] == "x":
            stop = True
            lst.pop()
    print(inf_list(lst))
    

elif choice == 5:
    print("Affiche l'ensemble des données d'un dictionnaire.")
    test_cara = test_bool(
                    input("Voulez-vous ajouter une chaîne de caractères ?\n"
                          "Oui: 1 / Non: 0 : ")
                )
    if test_cara:
        cara = input("Veuillez entrer votre chaîne: ")
    else:
        cara = ""
    
    print("Entrez vos key et value du dictionnaire (x pour arrêter): ")
    dico = {}
    while True:
        key = input("Key: ")
        if key == "x":
            break
        dico.update({key:input(f"Value ({key}): ")})
    
    dictionnaire(dico, cara)
