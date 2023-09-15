from sys import exit
from classes import Point, Cercle, Rectangle
    

def main():    
    '''
        Test de la classe Point.
    '''
    p1 = Point()
    print(p1)

    p2 = Point(2,6)
    print(p2)

    print(p1.distance(p2))
    print(p2.distance(2, 9))

    '''
        Test de la classe Cercle.
    '''
    c1 = Cercle(3)
    print(c1)

    c2 = Cercle(4, p2)
    print(c2)

    print(c1.diametre())
    print(c2.perimetre())
    print(c1.surface())
    print(c1.intersection(c2))
    print(c2.appartient(p1))


if __name__ == "__main__":
    exit(main())