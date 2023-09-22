#Naam:                      Marlo Halatoe
#Titel:                     Raad het getal
#Doel:                      Het raden van een willekeurig getal, gekozen door de computer
#Python versie:             3
#Gebruikte IDE:             Wing 101 (versie 9.1.1.1)
#Datum laatste bewerking:   06/09/2023

import sys
 for arg in sys.argv:
     print('[' + arg + ']')

# Getallen raden
import random       # Random library gebruiken

# Initialiseren
max_pogingen = 10   # Maximaal aantal pogingen om het getal te raden
bovengrens = 100 # Bovengrens voor het raden van het getal

# Kies een willekeurig getal tussen 1 en de bovengrens
antwoord = random.randint(1, bovengrens)

print('Raad een getal onder de 100.')
poging = 0                                                  # Het aantal pogingen begint bij 0
while True:                                                 # Laat de loop lopen zodat de gebruiker kan blijven raden
    getal = int(input('Geef een getal: '))
    while getal != antwoord and poging < max_pogingen -1:   # Indien getal niet geraden en het aantal pogingen < max_pogingen -1
        poging+=1       
        if getal < antwoord:                                # Indien getal lager ligt dan antwoord: Print 'hoger'!     
            print('Hoger!')
            break                                           # Herstart de loop
        elif getal > antwoord:                              # Indien getal hoger ligt dan antwoord: 'Print lager'!
            print('Lager!')
            break                                           # Herstart de loop
    
    else:
        if getal == antwoord:                               # Antwoord goed geraden
            poging+=1                                       # Ook bij de eerste keer raden = poging +1
            if poging ==1:
                print('Goed geraden! En dat in {} poging!'.format(poging))   # Print zin bij poging = 1
            else:
                print('Goed geraden! En dat in {} pogingen!'.format(poging)) # Print zin bij poging > 1
        else:
            #poging > max_pogingen:
            print('Helaas, u heeft het getal niet geraden.')                # Indien max pogingen is overschreden
        break
