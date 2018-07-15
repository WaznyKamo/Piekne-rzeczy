# Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.

kwota_pocz = input("Podaj kwotę w wartości liczbowej: ")
kwota = float(kwota_pocz)
liczba_5 = 0
liczba_2 = 0
liczba_1 = 0
liczba_05 = 0
liczba_02 = 0
liczba_01 = 0

def piataki(kwota, liczba_5 = 0):      #funkcja sprawdzająca ile w kwocie mieści
    while kwota >= 5:                    #się piątek i zwracająca kwotę bez nich
        kwota = kwota - 5
        liczba_5 = liczba_5 + 1
    return (kwota, liczba_5)

def dwoje(kwota, liczba_2 = 0):
    while kwota >= 2:
        kwota = kwota - 2
        liczba_2 = liczba_2 + 1
    return (kwota, liczba_2)

def zlotowki(kwota, liczba_1 = 0):
    while kwota >= 1:
        kwota = kwota - 1
        liczba_1 = liczba_1 + 1
    return (kwota, liczba_1)

def piecdziesiatki(kwota, liczba_05 = 0):
    while kwota >= 0.5:
        kwota = kwota - 0.5
        liczba_05 = liczba_05 + 1
    return (kwota, liczba_05)

def dwudziestki(kwota, liczba_02 = 0):
    while kwota >= 0.2:
        kwota = kwota - 0.2
        liczba_02 = liczba_02 + 1
    return (kwota, liczba_02)

def dziesiatki(kwota, liczba_01 = 0):
    while kwota >= 0.1:
        kwota = kwota - 0.1
        liczba_01 = liczba_01 + 1
    return (kwota, liczba_01)

if kwota >= 5:
    kwota, liczba_5 = piataki(kwota)
if kwota >= 2:
    kwota, liczba_2 = dwoje(kwota)
if kwota >= 1:
    kwota, liczba_1 = zlotowki(kwota)
if kwota >= 0.5:
    kwota, liczba_05 = piecdziesiatki(kwota)
if kwota >= 0.2:
    kwota, liczba_02 = dwudziestki(kwota)
if kwota >= 0.1:
    kwota, liczba_01 = dziesiatki(kwota)


print("W {} miesci się {}x5zł, {}x2zł, {}x1zł, {}x50gr, {}x20gr i {}x10gr"
      .format(kwota_pocz, liczba_5, liczba_2, liczba_1, liczba_05, liczba_02, liczba_01))