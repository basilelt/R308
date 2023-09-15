class Tasse:
    __matiere : str = "céramique"

    def __init__(self, color:str, size:float, brand:str):
        self.__color : str = color
        self.__size : float = size
        self.__brand : str = brand
    
    def __str__(self) -> str:
        return f"La tasse de matière {self.__matiere}, de couleur {self.__color} et de marque {self.__brand} a une contenance de {self.__size} mL."
    

    def add_content(self, content):
        self.__content : str = content

    def get_content(self):
        return self.__content
    
    def drink_content(self):
        del self.__content

maTasse = Tasse("bleue", 50, "duralex")
print(maTasse)

maTasse.add_content("café")
print(maTasse.get_content())

maTasse.drink_content
print(maTasse.get_content())




