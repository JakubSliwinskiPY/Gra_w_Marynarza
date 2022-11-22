import random

i = 0

wynik = 0
wynikpc = 0

papier = 4
kamien = 5
nozyce = 6

while i == 0:

    marynarz = random.randint(4, 6)

    print("""
    GRA W MARYNARZA
    Papier = 1
    Kamien = 2
    Nozyce = 3
    """)
    wybor = int(input("Wybierz opcje: "))
    #papier
    if wybor == 1 and marynarz == 4:
        print("Wybrałeś papier, komputer wylosował papier")
        print("REMIS")
        print("Gracz: ", wynik, "- Komputer: ", wynikpc, "\n")
    if wybor == 1 and marynarz == 5:
        print("Wybrałeś papier, komputer wylosował kamień")
        print("WYGRAŁEŚ")
        wynik += 1
        print("Gracz: ", wynik, "- Komputer: ", wynikpc, "\n")
    if wybor == 1 and marynarz == 6:
        print("Wybrałeś papier, komputer wylosował nożyce")
        print("PRZEGRAŁEŚ")
        wynikpc += 1
        print("Gracz: ", wynik, "- Komputer: ", wynikpc, "\n")
    #kamień
    if wybor == 2 and marynarz == 4:
        print("Wybrałeś kamień, komputer wylosował papier")
        print("PRZGERAŁEŚ")
        wynikpc += 1
        print("Gracz: ", wynik, "- Komputer: ", wynikpc, "\n")
    if wybor == 2 and marynarz == 5:
        print("Wybrałeś kamień, komputer wylosował kamień")
        print("REMIS")
        print("Gracz: ", wynik, "- Komputer: ", wynikpc, "\n")
    if wybor == 2 and marynarz == 6:
        print("Wybrałeś kamień, komputer wylosował nożyce")
        print("WYGRAŁEŚ")
        wynik += 1
        print("Gracz: ", wynik, "- Komputer: ", wynikpc, "\n")
    #nożyce
    if wybor == 3 and marynarz == 4:
        print("Wybrałeś nożyce, komputer wylosował papier")
        print("WYGRAŁEŚ")
        wynik += 1
        print("Gracz: ", wynik, "- Komputer: ", wynikpc, "\n")
    if wybor == 3 and marynarz == 5:
        print("Wybrałeś nożyce, komputer wylosował kamień")
        print("PRZEGRAŁEŚ")
        wynikpc += 1
        print("Gracz: ", wynik, "- Komputer: ", wynikpc, "\n")
    if wybor == 3 and marynarz == 6:
        print("Wybrałeś nożyce, komputer wylosował nożyce")
        print("REMIS")
        print("Gracz: ", wynik, "- Komputer: ", wynikpc, "\n")
    if wybor > 3:
        print("Nie ma takiej opcji")
