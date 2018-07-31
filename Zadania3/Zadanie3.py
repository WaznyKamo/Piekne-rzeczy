
def dodawanie_wpisu(pamietnik):
    wpis["data"] = input("Podaj datę wpisu:")
    wpis["zawartosc"] = input("Podaj treść wpisu")
    pamietnik.append(wpis)
    file.write("\ndata: " + wpis['data'] + '\n')
    file.write(wpis['zawartosc'] + '\n')


def wyswietlanie_wpisow(pamietnik):
    for wpis in pamietnik:
        print("data: " + wpis["data"])
        print("treść: " + wpis["zawartosc"])


def wpisy_daty(pamietnik):
    data = input("Podaj datę:")
    for wpis in pamietnik:
        if wpis["data"] == data:
            print(wpis['zawartosc'])
    print("Brak więcej wpisów w określonej dacie \n")


def przegladanie(pamietnik):
    i = 0
    while i <= len(pamietnik):
        print("data: " + pamietnik[i]["data"])
        print("treść: " + pamietnik[i]["zawartosc"])
        while True:
            decyzja = input("Wciśnij: \n 1->następny wpis\n 2->poprzedni wpis \n")
            if decyzja == "1":
                i += 1
                break
            elif decyzja == "2":
                i -= 1
                break
            else:
                print("Podano błędną wartość")

pamietnik = []
file = open("pamietnik.txt", "r+")
for line in file:
    wpis = {"data": "", "zawartosc": ""}
    if "data" in line:
        wpis["data"] = line.replace("data: ", '').replace("\n", '')
        for line in file:
            if line != "\n":
                wpis["zawartosc"] = wpis["zawartosc"] + line
            else:
                break

        pamietnik.append(wpis)

while True:
    decyzja = input("Co chciałbyś wykonać?: \n "
                    "1->dodać wpis \n "
                    "2->wyświetlić wszystkie wpisy \n "
                    "3->wyświetlić wszystkie wpisy pod określoną datą \n "
                    "4->przeglądać pojedyncze wpisy \n "
                    "5->zatrzymanie programu \n ")
    if decyzja == "1":
        dodawanie_wpisu(pamietnik)
    elif decyzja == "2":
        wyswietlanie_wpisow(pamietnik)
    elif decyzja == "3":
        wpisy_daty(pamietnik)
    elif decyzja == "4":
        przegladanie(pamietnik)
    elif decyzja == "5":
        file.close()
        break
    else:
        continue