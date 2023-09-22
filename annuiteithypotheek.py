import sys     
for arg in sys.argv:
     print('[' + arg + ']')

def annuiteit():
    geleend_bedrag = int(input('Geleend bedrag: '))             #Vraag het geleende bedrag
    aantal_term = 12 * (int(input('Aantal jaren aflossen: ')))  #Het aantal termijnen in maanden (12 * jaren)
    maandrente = ((float(input('Rente: '))/12)/100)             #De rente over het totaalbedrag wordt hier verrekend naar het rente bedrag per maand
    maand_bedrag = (maandrente / (1 - (1 + maandrente)** -aantal_term)) * geleend_bedrag    #formule voor het berekenen van het maandbedrag, afhankelijk van het geleende bedrag, aantal termijnen en de rente
    
    return '{:.2f}'.format(maand_bedrag)    # Geef het maandbedrag/termijnbedrag terug in 2 decimalen achter de komma

maandlast = annuiteit()

print('Uw maandlasten zijn: €',maandlast,'.')   #Druk de maandlasten af