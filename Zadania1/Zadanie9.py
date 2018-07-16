#9. Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7
liczba=int(input("Podaj liczbę: "))
if liczba%3==0 & liczba%5==0 & liczba%7==0:
    print("Liczba jest podzielna przez 3, 5 i 7")
else:
    print("Liczba nie jest podzielna przez 3, 5 i 7")
