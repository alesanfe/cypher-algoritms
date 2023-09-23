class XORCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        """
        Encrypts a message using a key.

        Args:
            message (bytes): The message to be encrypted.

        Returns:
            bytes: The encrypted message.
        """
        encrypted_message = bytearray()

        # Iterate over each byte in the message
        for i in range(len(message)):
            byte_message = message[i]
            byte_key = self.key[i % len(self.key)]  # Cycle the key if it is shorter than the message

            # XOR the message byte with the key byte
            byte_encrypted = byte_message ^ byte_key

            # Append the encrypted byte to the encrypted message
            encrypted_message.append(byte_encrypted)

        return bytes(encrypted_message)

    def decrypt(self, encrypted_message):
        """
        Decrypts an encrypted message using the encrypt method.

        Args:
            encrypted_message (str): The encrypted message to be decrypted.

        Returns:
            str: The decrypted message.
        """
        # The XOR operation is its own inverse
        return self.encrypt(encrypted_message)

if __name__ == '__main__':
    # Usage example
    key = b"SECRET_KEY"  # La clave XOR debe ser bytes
    cipher = XORCipher(key)

    original_message = b"Hello, XOR!"
    encrypted_message = cipher.encrypt(original_message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = cipher.decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message)
