#Naam:                      Marlo Halatoe
#Titel:                     ontbinden van getal in priemgetal(len)
#Doel:                      Het ontbinden van een ingegeven getal in priemgetallen
#Python versie:             3
#Gebruikte IDE:             Wing 101 (versie 9.1.1.1)
#Datum laatste bewerking:   06/09/2023

value = int(input(' Geef een getal: '))                 # Laat de gebruiker een getal ingeven
count_Priem = 2                                         # Het kleinste priemgetal. Er wordt uitgegaan dat elk getal een priemgetal kan zijn

while count_Priem <= value:                             # Hierdoor worden ingegeven getallen < 2 genegeerd
    if value % count_Priem == 0:                        # Indien het getal gedeeld kan worden met het priemgetal en restwaarde = 0
        print(count_Priem, end=' ')                     # print het priemgetal
        value /= count_Priem                            # ontbind het ingegeven getal met het priemgetal. De restwaarde wordt getal
    else:
        count_Priem += 1                                # probeer het volgende priemgetal
