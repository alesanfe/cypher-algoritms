# This is a sample Python script.
from src.main.python.algorithms.caesar import CaesarCipher
from src.main.python.algorithms.rail import RailFenceCipher
from src.main.python.algorithms.scytala import ScytaleCipher

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



if __name__ == '__main__':
    route = RailFenceCipher.from_path('src/test/resources/ruta.txt', '|')
    text = open('src/test/resources/texto.txt', 'r').read()

    print('*ORIGINAL TEXT:')
    print(text)

    rail = RailFenceCipher(route)
    caesar = CaesarCipher(3)
    scytale = ScytaleCipher(3)

    print('\n+++ENCRYPTING!!!!')

    encrypted = rail.encrypt(text)
    print('+Rail encryption:')
    print(encrypted)

    encrypted = scytale.encrypt(encrypted)
    print('+Scytale encryption:')
    print(encrypted)

    encrypted = caesar.encrypt(encrypted)
    print('+Caesar encryption:')
    print(encrypted)


    print('\n---DECRYPTING!!!!')

    desencrypted = caesar.decrypt(encrypted)
    print('-Caesar decryption:')
    print(desencrypted)

    desencrypted = scytale.decrypt(desencrypted)
    print('-Scytale decryption:')
    print(desencrypted)

    desencrypted = rail.encrypt(desencrypted)
    print('-Rail decryption:')
    print(desencrypted)
