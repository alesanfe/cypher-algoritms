from dataclasses import dataclass


class RailFenceCipher:
    def __init__(self, path_text, path_rail):
        self.path_text = path_text
        self.path_rail = path_rail
        self.text = open(self.path_text, "r").read()
        self.rail = open(self.path_rail, "r").read()
        if len(self.text) != len(self.rail):
            raise Exception("El texto y la ruta deben tener la misma longitud")

    def encrypt(self):
        """
        Encrypts the text using the rail fence cipher.

        Returns:
            str: The encrypted text.

        Raises:
            None
        """
        encrypted_text = [''] * len(self.rail)
        rail_positions = [int(rail) if rail.isdigit() else -1 for rail in self.rail]

        for i, char in enumerate(self.text):
            rail = rail_positions[i % len(rail_positions)]
            if rail != -1:
                encrypted_text[rail] += char
            else:
                encrypted_text[i % len(encrypted_text)] += '\n'

        return ''.join(encrypted_text)

    def decrypt(self):
        """
        Decrypts the given text using the rail fence cipher algorithm.

        Parameters:
            None.

        Returns:
            str: The decrypted text.

        Algorithm:
            - Create an empty list of the same length as the input text called `decrypted_text`
            - Convert the rail positions to integers or -1 if not a digit
            - Set `char_index` and `rail_index` to 0
            - Iterate over each character in the input text
                - Get the rail position for the current rail index
                - If the rail position is not -1, assign the current character to `decrypted_text` at the `char_index`
                - If the rail position is -1, assign a newline character to `decrypted_text` at the `char_index`
                - Increment `char_index` by 1
                - Increment `rail_index` by 1, wrapping around to 0 if necessary
            - Join the `decrypted_text` list into a string and remove any trailing whitespace
            - Return the decrypted text
        """
        decrypted_text = [' '] * len(self.text)
        rail_positions = [int(rail) if rail.isdigit() else -1 for rail in self.rail]
        char_index = 0
        rail_index = 0

        for char in self.text:
            rail = rail_positions[rail_index]
            decrypted_text[char_index] = char if rail != -1 else '\n'
            char_index += 1
            rail_index = (rail_index + 1) % len(self.rail)

        return ''.join(decrypted_text).rstrip()  # Eliminamos espacios en blanco adicionales y luego rstrip para preservar los saltos de línea


# Example usage:
if __name__ == '__main__':
    # Crear una instancia de RailFenceCipher con los archivos de texto y riel
    cipher = RailFenceCipher("texto.txt", "ruta.txt")

    # Cifrar el mensaje
    ciphertext = cipher.encrypt()
    print("Texto cifrado:")
    print(ciphertext)
    print()

    # Descifrar el mensaje
    decrypted_text = cipher.decrypt()
    print("Texto descifrado:")

    print(decrypted_text)


