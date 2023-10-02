'''
functions that will check if a .bmp file is a valid bmp file and will reads the width and height from the bmp file
'''
import struct
def bmp_read(filename):
    f = open (filename, 'rb')               # open the file in binairy read modus
    bytes = f.read(26)                      # read the file till byte number 26
    pixelWidth = bytes[18:22]               # read from byte 18 (0012h) till byte 22 (0016h)
    pixelHeight = bytes[22:26]              # read from byte 22 (0016h) till byte 26 (0019h)
    f.close()                               # close the file

    #4-byte Little Endian Format convert to long int
    def lef_int(tekens):
        value = struct.unpack('<L', tekens)[0]
        return value
    
    tup = (lef_int(pixelWidth),lef_int(pixelHeight))  #create a tuple
    print ('The width of the bmp file is {} pixels and the height of the file is {} pixels'.format(tup[0],tup[1]))

'''
function that checks if the file is a valid bmp file
'''
def sig_check(filename):            
    f = open (filename, 'rb')      
    signature = f.read (2)              # hang het lezen van f aan variabele signature
    if signature != b'BM':              # controleer of het bestand een geldige BMP-indeling heeft
        print('file is not a valid bmp file')
    f.close()
        

bmp_read('loi_logo.bmp')
sig_check('loi_logo.bmp')
