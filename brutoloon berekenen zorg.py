brutoloon = int(input('Geef je brutoloon op: '))                    #conform CAO ziekenhuizen, zie betreffende schaal/trede
gewerkte_uren = int(input('Geef het aantal gewerkte uren in de maand op: '))
uurloon = brutoloon / gewerkte_uren                                           #uurloon op basis van 36-urige werkweek
ort22 = 0.22 * uurloon * int(input('Aantal uren ort 22%: '))
ort38 = 0.38 * uurloon * int(input('Aantal uren ort 38%: '))
ort47 = 0.47 * uurloon * int(input('Aantal uren ort 47%: '))
ort60 = 0.60 * uurloon * int(input('Aantal uren ort 60%: '))

totaal = brutoloon + ort22 + ort38 + ort47 + ort60

print('Totaal brutoloon is: €', '{:.2f}'.format(totaal))

