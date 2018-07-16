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

def funkcja():
    napis = "0"
    wynik = 0

    while True:
        liczba = input("Podaj liczbę, jeśli chcesz poznać sumę podanych liczb, wpisz STOP: ")
        dlugosc = len(liczba)
        napis = napis + "+" + liczba

        try:
            liczba_f = float(liczba)
        except ValueError:
            if liczba == "STOP":
                break
            else:
                print("Podano błędną wartość")
                continue
        print(napis)
        wynik = wynik + liczba_f

    print("Twoj wynik to {}".format(wynik))


funkcja()
while True:
    decyzja = input("Czy chcesz rozpocząć jeszcze raz? Tak/Nie: ")
    if decyzja == "Tak":
        funkcja()
    elif decyzja == "Nie":
        break
    else:
        print("Podano błędną wartość")
        continue