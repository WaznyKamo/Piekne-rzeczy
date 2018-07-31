import csv

szerokosc_kolumny = 20

csvfile = open('adresy.csv', "r+" ,newline="")
dane = list(csv.reader(csvfile))
keys = dane.pop(0)                              #odczytuje klucze z pierwszej linii tekstu, resztę zwraca jako dane
dane_tabeli = []

print(("+" + szerokosc_kolumny * "-") * len(keys) + "+")
for key in keys:
    if len(key) >= szerokosc_kolumny:                               #wyświetlanie nagłówków tabeli z zm. keys
        print("|" + key[0:(szerokosc_kolumny-3)] + '...', end="")
    else:
        print("|" + key + (szerokosc_kolumny - len(key)) * " ", end="")
print("|")
print(("+" + szerokosc_kolumny * "-") * len(keys) + "+")

for wiersz in dane:                             #dla każdego wiersza zwraca słownik
    slownik = {}                                #każda dana słownika ma przypisaną klasę i wartość
    for i, dana in enumerate(wiersz):
        slownik[keys[i]] = dana
        if len(dana) >= szerokosc_kolumny:
            print("|" + dana[0:(szerokosc_kolumny-3)] + '...', end="")
        else:
            print("|" + dana + (szerokosc_kolumny - len(dana)) * " ", end="")
    print("|")
    print(("+" + szerokosc_kolumny * "-") * len(keys) + "+")
    dane_tabeli.append(slownik)                 #po utworzeniu słownika dodaje go jako kolejną wartość do listy (zm. dane)
csvfile.close()