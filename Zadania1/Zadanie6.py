#Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny. Załóż że wpisywane jest zawsze tylko 6 znaków 0/1, np 000110, 110010, 111111 etc
binarna=input ("Podaj liczbe binarna")
cyfra=int (binarna[5])
liczba = (int (binarna[5]))*1+(int (binarna[4]))*2+(int(binarna[3]))*4+(int(binarna[2]))*8+(int(binarna[1]))*16+(int(binarna[0]))*32
print(liczba)