#4. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
liczba=input("Podaj liczbę: ")
liczba_znakow=len(liczba)
print("Pierwsza cyfra to: ", liczba[0])
print("Ostatnia cyfra to: ", liczba[liczba_znakow-1])