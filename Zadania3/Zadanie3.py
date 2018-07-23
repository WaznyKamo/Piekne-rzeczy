
def dodawanie_wpisu():
    pass


def wyswietlanie_wpisow():
    pass


def wpisy_daty():
    pass


def przegladanie():
    pass

pamietnik = []
file = open("pamietnik.txt", "r+")
for line in file:
    wpis = {"data": "", "zawartosc": ""}
    if "data" in line:
        wpis["data"] = line.replace("data: ", '')
        print(wpis["data"], end='')
        for line in file:
            if line != "\n":
                wpis["zawartosc"] = wpis["zawartosc"] + line
            else:
                print(wpis["zawartosc"])
                break
        pamietnik.append(wpis)
print(pamietnik)