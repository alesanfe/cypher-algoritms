from dataclasses import dataclass


@dataclass
class ScytaleCipher:
    num_rows: int

    def encrypt(self, text: str) -> str:
        """
            Encrypts the given plaintext using the Rail Fence Cipher.

            Parameters:
                text (str): The text to be encrypted.

            Returns:
                str: The encrypted ciphertext.
        """
        text += ' ' * (self.num_rows - len(text) % self.num_rows)  # Add spaces to complete the last row
        ciphertext = ""
        for col in range(self.num_rows):
            for i in range(col, len(text), self.num_rows):
                ciphertext += text[i]
        return ciphertext

    def decrypt(self, text) -> str:
        """
        Decrypts the given ciphertext using a transposition cipher.

        Parameters:
            text (str): The encrypted text to be decrypted.

        Returns:
            str: The decrypted plaintext.

        Note:
            This function assumes that the ciphertext was encrypted using a transposition cipher.
            The transposition cipher works by rearranging the characters of the plaintext in a specific way.
            The decryption process involves rearranging the characters of the ciphertext back to their original order.

            The decrypted plaintext may contain additional spaces at the end due to the nature of the transposition cipher.
            To remove these extra spaces, use the `strip()` method on the decrypted plaintext before using it.

        Example:
            >>> cipher = TranspositionCipher(num_rows=3)
            >>> ciphertext = cipher.encrypt("Hello, world!")
            >>> plaintext = cipher.decrypt(text)
            >>> print(plaintext)
            Hello, world!

        """
        num_columns = len(text) // self.num_rows
        plaintext = ""
        for col in range(num_columns):
            for i in range(col, len(text), num_columns):
                plaintext += text[i]
        return plaintext.strip()  # Remove added spaces during decryption
