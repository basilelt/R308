from math import sqrt, pi
from typing import Union


class Point:
    def __init__(self, x:float = 0, y:float = 0):
        '''
            Initialiser les coordonnées au point origine (0,0) ou à des données passées en arguments.
        '''
        if isinstance(x, Union[int, float]) and isinstance(y, Union[int, float]):
            self.__x:float = x
            self.__y:float = y
        
        else:
            raise TypeError("x ou y n'est pas un int ou un float.")
    
    def __str__(self):
        return f"Le point à pour coordonnées ({self.__x};{self.__y})"


    def distance(self, *args) -> float:
        '''
            Calculer la distance entre 2 points en passant les coordonnées en arguments.
        '''
        if len(args) > 2:
            raise ValueError("Il y a plus d'arguments fournis que nécessaire.")
        
        elif len(args) == 1 and isinstance(args[0], Point):
            dist = sqrt( (args[0].get_x() - self.__x)**2 + (args[0].get_y() - self.__y)**2 )
        
        elif len(args) == 2 and isinstance(args[0], Union[int, float]) and isinstance(args[1], Union[int, float]):
            dist = sqrt( (args[0] - self.__x)**2 + (args[1] - self.__y)**2 )
        
        else:
            raise TypeError("x ou y n'est pas un int ou un float.")

        return dist
        
    
    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y
    

class Cercle:
    def __init__(self, r:float, centre:Point = Point()):
        '''
            Initialiser les coordonnées du cercle.
        '''
        if isinstance(centre, Point) and isinstance(r, Union[int, float]):
            self.__centre = centre
            self.__r = r
        else:
            raise TypeError("Le rayon n'est pas un int ou un float ou le centre n'est pas un point.")
    
    def __str__(self):
        return f"Le cercle à pour rayon {self.__r} et comme centre ({self.__centre.get_x()};{self.__centre.get_y()})"
    

    def diametre(self) -> float:
        return (2 * self.__r)
    
    def perimetre(self) -> float:
        return (2 * pi * self.__r)
    
    def surface(self) -> float:
        return (pi * (self.__r**2))
    
    def intersection(self, cercle2:'Cercle') -> bool:
        if isinstance(cercle2, Cercle):
            if self.__centre.distance(cercle2.get_centre()) < (self.__r + cercle2.get_rayon()):
                return True
            else:
                return False
        
        else:
             raise TypeError("Le cercle donné n'est pas un cercle.")
    
    def appartient(self, point:Point) -> bool:
        if isinstance(point, Point):
            if self.__centre.distance(point) < self.__r:
                return True
            else:
                return False
        
        else:
             raise TypeError("Le point donné n'est pas un point.")

    
    def get_centre(self) -> Point:
        return self.__centre

    def get_rayon(self) -> float:
        return self.__r         


class Rectangle:
    def __init__(self, pbg:Point = Point(), longueur:float = 1, hauteur:float = 1, phd:Point = None):
        if isinstance(pbg, Point):
            self.__pbg = pbg
            
            if phd == None:
                self.__longueur = longueur
                self.__hauteur = hauteur
                
                self.__phd = Point(pbg.get_x() + longueur, pbg.get_y() + hauteur)
                self.__phg = Point(pbg.get_x(), pbg.get_y() + hauteur)
                self.__pbd = Point(pbg.get_x() + longueur, pbg.get_y())
            
            elif isinstance(phd, Point):
                self.__longueur = sqrt( (pbg.get_x() - phd.get_x())**2 )
                self.__hauteur = sqrt( (pbg.get_y() - phd.get_y())**2 )
                
                self.__phd = phd
                self.__phg = Point(pbg.get_x(), pbg.get_y() + hauteur)
                self.__pbd = Point(pbg.get_x() + longueur, pbg.get_y())

            else:
                raise TypeError("Le point donné n'est pas un point.")
        
        else:
            raise TypeError("Le point donné n'est pas un point.")
        
        
    def surface(self) -> float:
        return self.__longueur * self.__hauteur
    
    def perimetre(self) -> float:
        return self.__longueur * 2 + self.__hauteur * 2
    
    def position(self) -> list:
        return [self.__pbg, self.__pbd, self.__phd, self.__phg]
    
    def appartient(self, p) -> bool:
        if isinstance(p, Point):
            if (self.__pbg <= p.get_x() <= self.__pbd) and (self.__phg <= p.get_y() <= self.__phd):
                return True
            else:
                return False
        
        else: 
            raise TypeError("Le point donné n'est pas un point.")


class Triangle:
    def __init__(self, ):
        return