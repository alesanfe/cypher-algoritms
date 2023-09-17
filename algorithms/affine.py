from dataclasses import dataclass
from typing import Optional


@dataclass
class AffineCipher:
    a: int  # Multiplicative coefficient
    b: int  # Additive term
    m: int  # Size of the alphabet

    def gcd(self, a: int, b: int) -> int:
        """
        Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The GCD of the two numbers.
        """
        # Base case: if b is 0, return a
        if b == 0:
            return a

        # Recursive case: call gcd with b and a % b
        return self.gcd(b, a % b)

    def mod_inverse(self, a: int, m: int) -> Optional[int]:
        """
        Calculate the modular inverse of a number.

        Args:
            a (int): The number.
            m (int): The modulo.

        Returns:
            Optional[int]: The modular inverse of the number, or None if it does not exist.
        """
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def encrypt(self, text: str) -> str:
        """
        Encrypts the given text using an affine cipher.

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        encrypted_text = ''

        for char in text:
            if char.isalpha():  # Only encrypt letters and leave other characters unchanged
                is_upper = char.isupper()  # Check if the character is uppercase
                char = char.lower()  # Convert to lowercase for encryption
                char_code = ord(char) - ord('a')  # Get the ASCII value of the character in [0, 25]
                char_code = (self.a * char_code + self.b) % self.m  # Apply the affine cipher
                char = chr(char_code + ord('a'))  # Convert back to character
                if is_upper:  # If the original character was uppercase, convert to uppercase
                    char = char.upper()
            encrypted_text += char

        return encrypted_text

    def decrypt(self, text: str) -> str:
        """
        Decrypts the given text using the affine cipher.

        Args:
            text (str): The text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        decrypted_text = ''
        a_inverse = self.mod_inverse(self.a, self.m)  # Calculate the modular inverse of 'a'

        if a_inverse is None:
            raise ValueError("The modular inverse of 'a' does not exist.")

        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                char_code = ord(char) - ord('a')  # Convert the character to its corresponding code
                char_code = (a_inverse * (char_code - self.b)) % self.m  # Apply the decryption formula of the affine cipher
                char = chr(char_code + ord('a'))  # Convert the code back to a character
                if is_upper:
                    char = char.upper()
            decrypted_text += char

        return decrypted_text


# Example usage:
if __name__ == '__main__':
    # Crear una instancia de CaesarCipher con el desplazamiento
    cipher = AffineCipher(1, 3, 26)

    # Cifrar el mensaje
    ciphertext = cipher.encrypt("Hello, world!")
    print("Texto cifrado:", ciphertext)
    print()

    # Descifrar el mensaje
    plaintext = cipher.decrypt(ciphertext)
    print("Texto descifrado:", plaintext)
