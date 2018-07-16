#8. Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7
liczba=int(input("Podaj liczbę: "))
if liczba%3==0 or liczba%5==0 or liczba%7==0:
    if liczba%3==0:
        print("Liczba jest podzielna przez 3")
    if liczba%5==0:
        print("Liczba jest podzielna przez 5")
    if liczba%7==0:
        print("Liczba jest podzielna przez 7")
else:
    print("Liczba nie jest podzielna przez 3, 5 lub 7")