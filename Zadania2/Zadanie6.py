# 6) Napisz kalkulator, który będzie przyjmował do operacji dowolną ilość liczb, tak długo do póki nie wpiszę np słowa "DOŚĆ" :)
#    Za każdym wpisaniem liczby niech wyświetla operację liczby które będzie brał do wyliczeń
#    MENU: 1/2/3/4/5/6/kolejne operacjie
#    Operacja: jakiś wybór z menu
#    Wprowadz liczbe: 1
#    1
#    Wprowadz liczbe: 2
#    1 + 2
#    Wprowadz liczbe: 13
#    1 + 2 + 13
#    Wprowadz liczbe: DOŚĆ
#    Twój wynik to 16.
#    Czy chcesz wykonać jeszcze jakieś obliczenia? "T", powraca do menu "N" zamyka program

napis = "0"
wynik = 0

while True:
    liczba = input("Podaj liczbę, jeśli chcesz poznać sumę podanych liczb, wpisz STOP: ")
    dlugosc = len(liczba)
    napis = napis + "+" +liczba
    if liczba == "STOP":
        break
    else:
        for i in range(0, dlugosc):
            if liczba[0].isdigit() or liczba[0] == ".":
                pass
            else:
                print("Podano złą wartość")
                break
        liczba = int(liczba)
    print(napis)
    wynik = wynik + liczba

print ("Twoj wynik to {}".format(wynik))