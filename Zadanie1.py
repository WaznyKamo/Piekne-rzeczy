# #1) Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)

parametr = ['col13221321311', 'col2', 'col3', 'col4', 'col5']
liczba_wyrazow = len(parametr)
szerokosc_kolumny = 10
i = 0

print(("+" + szerokosc_kolumny * "-") * liczba_wyrazow + "+")
for i in range(liczba_wyrazow):
    if len(parametr[i]) >= szerokosc_kolumny:
        i1 = 0
        print("|", end="")
        for i1 in range(szerokosc_kolumny - 3):
            print(parametr[i][i1], end="")
        print("...", end="")
    else:
        print("|%s" %parametr[i] + (szerokosc_kolumny - len(parametr[i])) * " ", end="")
    i += 1
print("|")
print(("+" + szerokosc_kolumny * "-") * liczba_wyrazow + "+")