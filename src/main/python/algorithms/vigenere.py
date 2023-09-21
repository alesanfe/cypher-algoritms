
class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def encrypt(self, message):
        """
        Encrypts a given message using a repeating key.

        Parameters:
        message (str): The message to be encrypted.

        Returns:
        str: The encrypted message.
        """
        encrypted_message = ""
        key_repeated = self.key * (len(message) // len(self.key)) + self.key[:len(message) % len(self.key)]

        for i in range(len(message)):
            if message[i].isalpha():
                if message[i].isupper():
                    shift = ord(key_repeated[i]) - ord('A')
                    encrypted_message += chr((ord(message[i]) - ord('A') + shift) % 26 + ord('A'))
                else:
                    shift = ord(key_repeated[i]) - ord('A')
                    encrypted_message += chr((ord(message[i]) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_message += message[i]
        return encrypted_message

    def decrypt(self, encrypted_message):
        """
        Decrypts an encrypted message using a key.

        Args:
            encrypted_message (str): The encrypted message to decrypt.

        Returns:
            str: The decrypted message.
        """
        decrypted_message = ""
        key_repeated = self.key * (len(encrypted_message) // len(self.key)) + self.key[
                                                                              :len(encrypted_message) % len(self.key)]

        for i in range(len(encrypted_message)):
            if encrypted_message[i].isalpha():
                if encrypted_message[i].isupper():
                    shift = ord(key_repeated[i]) - ord('A')
                    decrypted_message += chr((ord(encrypted_message[i]) - ord('A') - shift) % 26 + ord('A'))
                else:
                    shift = ord(key_repeated[i]) - ord('A')
                    decrypted_message += chr((ord(encrypted_message[i]) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_message += encrypted_message[i]
        return decrypted_message

if __name__ == '__main__':
    # Usage example
    key = "KEY"
    cipher = VigenereCipher(key)

    original_message = "HELLOWORLD"
    encrypted_message = cipher.encrypt(original_message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = cipher.decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message)




