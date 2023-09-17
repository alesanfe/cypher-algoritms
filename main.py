# This is a sample Python script.
from algorithms.scytala import ScytaleCipher


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



if __name__ == '__main__':
    escitala = ScytaleCipher(3)
    mensaje = "ESTEESUNMENSAJESECRETO"
    cifrado = escitala.encrypt(mensaje)
    print("Texto cifrado:", cifrado)
    descifrado = escitala.decrypt(cifrado)
    print("Texto descifrado:", descifrado)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
