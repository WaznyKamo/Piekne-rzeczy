# #1) Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)

file = open("plik.txt", "r+")
list = file.read().splitlines()             #plik odczytuje każdą linijkę tekstu jako wartość, która ma być umieszczona w kolumnie
liczba_wyrazow = len(list)
szerokosc_kolumny = 20

print(("+" + szerokosc_kolumny * "-") * liczba_wyrazow + "+")
for i in range(liczba_wyrazow):
    if len(list[i]) >= szerokosc_kolumny:
        i1 = 0
        print("|", end="")
        for i1 in range(szerokosc_kolumny - 3):
            print(list[i][i1], end="")
        print("...", end="")
    else:
        print("|%s" %list[i] + (szerokosc_kolumny - len(list[i])) * " ", end="")
    i += 1
print("|")
print(("+" + szerokosc_kolumny * "-") * liczba_wyrazow + "+")