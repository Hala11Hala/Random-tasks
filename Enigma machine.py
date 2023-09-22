class Rotor:
    def __init__(self, wiring, notch):
        self.wiring = wiring
        self.notch = notch
        self.position = 'A'
        
    def set_position(self, position):
        self.position = position
        
    def substitute_forward(self, char):
        index = (ord(char) - ord('A') + ord(self.position) - ord('A')) % 26
        return self.wiring[index]
    
    def substitute_backward(self, char):
        index = (self.wiring.index(char) - ord(self.position) + ord('A')) % 26
        return chr(index + ord('A'))

class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring
        
    def reflect(self, char):
        return self.wiring[ord(char) - ord('A')]

class EnigmaMachine:
    def __init__(self, rotor1, rotor2, rotor3, reflector):
        self.rotors = [rotor1, rotor2, rotor3]
        self.reflector = reflector
        
    def set_rotor_positions(self, positions):
        for rotor, position in zip(self.rotors, positions):
            rotor.set_position(position)
            
    def encode_char(self, char):
        for rotor in self.rotors:
            char = rotor.substitute_forward(char)
        char = self.reflector.reflect(char)
        for rotor in reversed(self.rotors):
            char = rotor.substitute_backward(char)
        return char

    def encode_message(self, message):
        encoded_message = ""
        for char in message:
            if char.isalpha():
                encoded_char = self.encode_char(char.upper())
                encoded_message += encoded_char
                for i in range(len(self.rotors)-1):
                    if self.rotors[i].position == self.rotors[i].notch:
                        self.rotors[i+1].position = chr((ord(self.rotors[i+1].position) - ord('A') + 1) % 26 + ord('A'))
                self.rotors[0].position = chr((ord(self.rotors[0].position) - ord('A') + 1) % 26 + ord('A'))
        return encoded_message

def char_to_index(char):
    return ord(char.upper()) - ord('A')

def index_to_char(index):
    return chr(index + ord('A'))

def sanitize_input(input_text):
    return ''.join(filter(str.isalpha, input_text)).upper()

rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E')
rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V')
reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

enigma = EnigmaMachine(rotor1, rotor2, rotor3, reflector)

while True:
    choice = input("Do you want to encode or decode a message? (encode/decode/exit): ")
    if choice.lower() == "exit":
        break
    elif choice.lower() == "encode" or choice.lower() == "decode":
        input_message = input(f"Enter the message to {choice.lower()}: ")
        sanitized_message = sanitize_input(input_message)
        
        enigma.set_rotor_positions("AAA")
        if choice.lower() == "encode":
            encoded_message = enigma.encode_message(sanitized_message)
            print(f"Encoded message: {encoded_message}")
        else:
            decoded_message = enigma.encode_message(sanitized_message)  # Decoding is the same as encoding
            print(f"Decoded message: {decoded_message}")
    else:
        print("Invalid choice. Please enter 'encode', 'decode', or 'exit'.")
