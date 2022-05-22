import math

i = int(input()) #Liczba figur geometrycznych
x = 0
#figura = []
#figura.append(list(map(int,input().split())))



def Rozwiazanie():
    wynik = []
    for x in range(i):
        lista  = list(input().split())
        figura = list(map(lambda z: float(z), lista))

        if len(figura) == 1:
            pole = figura[0]**2*math.pi
            wynik.append(pole)
        elif len(figura) == 2:
            pole = figura[0] * figura[1]
            wynik.append(pole)
        elif len(figura) == 3:
            s = (figura[0]+figura[1]+figura[2])/ 2
            pole = s*(s-figura[0])*(s-figura[1])*(s-figura[2])
            pole = pole ** 0.5
            wynik.append(pole)
        elif len(figura) > 3:
            print("Błąd, można podać maksymalnie 3 liczby")
    wynik_suma = round(sum(wynik),2)
    print(wynik_suma)
    x += 1
        

Rozwiazanie()




