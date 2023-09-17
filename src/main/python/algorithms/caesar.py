from src.main.python.algorithms.affine import AffineCipher


class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift  # El número de lugares que se desplazan las letras
        self.algorithm = AffineCipher(1, shift, 26)

    def encrypt(self, text: str) -> str:
        """
        Encrypts the given text using a Caesar cipher.

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        return self.algorithm.encrypt(text)

    def decrypt(self, text):
        """
        Decrypts the given text using the Caesar cipher with the specified shift.

        Args:
            text (str): The text to decrypt.

        Returns:
            str: The decrypted text.
        """
        return self.algorithm.decrypt(text)
