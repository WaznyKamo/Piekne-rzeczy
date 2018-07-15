#4) Kalkulator do wyliczania wieku psa.
#   Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#   Np: 15 ludzkich lat to 73 psie lata

wartosc_podana = (input("Podaj wiek psa w ludzkich latach: "))
ludzki_wiek = int(wartosc_podana)
psi_wiek = 0

if ludzki_wiek >= 2:
    psi_wiek = 21
    ludzki_wiek = ludzki_wiek - 2
elif ludzki_wiek >= 1:
    psi_wiek = 10.5
    ludzki_wiek = ludzki_wiek - 1

psi_wiek = psi_wiek + 4 * ludzki_wiek

print(("{} w ludzkich latach to inaczej {} w psich latach").format(wartosc_podana, psi_wiek))