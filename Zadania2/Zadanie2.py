# Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.


nr_5 = nr_2 = nr_1 = nr_05 = nr_02 = nr_01 = 0  # definiowanie liczników monet

while True:
    starting_value = input("Podaj kwotę w wartości liczbowej: ")
    try:
        value = float(starting_value)
        break
    except ValueError:
        print("Podano nieprawidłową wartość")
        continue

while True:
    if value >= 5:
        value = value - 5
        nr_5 += 1
    elif value >= 2:
        value = value - 2
        nr_2 += 1
    elif value >= 1:
        value = value - 1
        nr_1 += 1
    elif value >= 0.5:
        value = value - 0.5
        nr_05 += 1
    elif value >= 0.2:
        value = value - 0.2
        nr_02 += 1
    elif value >= 0.1:
        value = value - 0.1
        nr_01 += 1
    else:
        break

print(("Kwota {}zł może zostać rozmieniona na:\n{}x5zł \n{}x2zł \n{}x1zł \n{}x50gr \n{}x20gr \n{}x10gr")
      .format(starting_value, nr_5, nr_2, nr_1, nr_05, nr_02, nr_01))
