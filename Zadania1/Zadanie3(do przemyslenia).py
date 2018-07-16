# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
print("Ten program oblicza powierzchnię koła, w zależności od promienia")
promien= input ("Podaj wartość promienia: ")

licznik =0
dlugosc=len(promien)
while licznik in (0, dlugosc-1):
    if promien[licznik] in string.letters:
        jednostka = promien.isletter

#pole= 3.14*wartosc_promienia**2
#print(pole, jednostka)
#print("3.14 *", promien,"^2=",pole)
#print("Pole wynosi: ",pole)