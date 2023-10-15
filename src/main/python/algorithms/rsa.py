import secrets


class RSACipher:

    def __init__(self, bits=2048, public_exponent=65537):
        """
        Initialize the RSA cipher with the specified number of bits and public exponent.

        :param bits: Number of bits for the RSA key (default is 2048).
        :param public_exponent: Public exponent value (default is 65537).
        """
        self.bits = bits
        self.public_exponent = public_exponent
        self.n, self.e, self.d = self.generate_key_pair()

    @staticmethod
    def is_prime(number, k=5):
        if number <= 3:
            return number > 1
        if number % 2 == 0:
            return False

        r, s = 0, number - 1
        while s % 2 == 0:
            r += 1
            s //= 2

        for _ in range(k):
            a = secrets.randbelow(number - 2) + 2
            x = pow(a, s, number)
            if x == 1 or x == number - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, number)
                if x == number - 1:
                    break
            else:
                return False

        return True

    @staticmethod
    def generate_prime(bits):
        while True:
            number = secrets.randbits(bits) | 1  # Odd number
            if RSACipher.is_prime(number):
                return number

    @staticmethod
    def gcd_extended(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = RSACipher.gcd_extended(b % a, a)
        return g, x - (b // a) * y, y

    @staticmethod
    def mod_inverse(a, m):
        g, x, _ = RSACipher.gcd_extended(a, m)
        if g != 1:
            raise ValueError("The modular inverse does not exist")
        return x % m

    def generate_key_pair(self):
        p = self.generate_prime(self.bits // 2)
        q = self.generate_prime(self.bits // 2)
        n = p * q
        phi_n = (p - 1) * (q - 1)
        e = self.public_exponent
        d = self.mod_inverse(e, phi_n)
        return n, e, d

    def encrypt(self, message):
        message_bytes = message.encode('utf-8')
        encrypted = [pow(byte, self.e, self.n) for byte in message_bytes]
        return encrypted

    def decrypt(self, encrypted_message):
        decrypted_bytes = [pow(byte, self.d, self.n) for byte in encrypted_message]
        decrypted_message = ''.join([chr(byte) for byte in decrypted_bytes])
        return decrypted_message


if __name__ == '__main__':
    cipher = RSACipher()
    message = "Hello, world"
    print("Original message:", message)
    encrypted_message = cipher.encrypt(message)
    print("Encrypted message:", encrypted_message)
    decrypted_message = cipher.decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message)
