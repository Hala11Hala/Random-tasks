import sys
for arg in sys.argv:
     print('[' + arg + ']')


def isPalindroom():

     woord = input('Geef een woord: ')   #Vraag de gebruiker om een woord
     omgekeerd = woord[::-1]             #Keer het gevraagde woord om

     for i in range(len(woord)-1):
          if woord[i] == omgekeerd[i]:
               palindroom = True
               continue
          else:
               print('Dit is geen palindroom!')
               palindroom = False
               break

     if palindroom == True:
          print('Dit is een palindroom!')

isPalindroom()