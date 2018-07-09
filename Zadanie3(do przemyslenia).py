# 3. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
print("Ten program oblicza powierzchnię koła, w zależności od promienia")
promien= input ("Podaj wartość promienia: ")

wartosc_promienia = int (promien)
jednostka = promien.isletter
pole= 3.14*wartosc_promienia**2
print(pole, jednostka)
#print("3.14 *", promien,"^2=",pole)
#print("Pole wynosi: ",pole)