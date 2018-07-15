#3) Program rysujący piramidę o określonej wysokości, np dla 3
      #
     ###
    #####

wysokosc =int (input("Podaj wysokość piramidy: "))
i=0
szerokosc_wiersza = 1
for i in range (0, wysokosc):
    print(('{:^20}').format(szerokosc_wiersza * "#"))
    i += 1
    szerokosc_wiersza = szerokosc_wiersza + 2
