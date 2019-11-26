from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class Encrypter:
    def __init__(self, block_len, cipher):
        self.block_len = block_len
        self.cipher = cipher

    def _pad(self, pt):
        str_pad = pt + chr(self.block_len - len(pt) % 16) * (self.block_len - len(pt) % self.block_len)
        return bytes(str_pad.encode('utf-8'))

    @staticmethod
    def _unpad(ct):
        byte_unpad = ct[:-ct[-1]]
        return byte_unpad.decode('utf-8')

    def encode(self, plain_text):
        if type(plain_text) is not bytes:
            plain_text = self._pad(plain_text)

        return self.cipher.encrypt(plain_text)

    def decode(self, crypted_text):
        temp = self.cipher.decrypt(crypted_text)
        return self._unpad(temp)


def int_input(text):
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print('\nYou have to input integer number\n')


if __name__ == '__main__':
    while True:
        choice = int_input('Choose the action:\n'
                           '\t1 - Complete task1\n'
                           '\t2 - Complete task2 \n'
                           '\t0 - Exit\n'
                           'Your choice: ')

        if choice < 0 or choice > 2:
            print('\nYour choice is out of range\n')
            continue
        elif choice == 1:
            plain_text = 'some_test_text'
            key_size = AES.key_size[2]
            block_size = AES.block_size

            key = get_random_bytes(key_size)
            cipher = AES.new(key, AES.MODE_ECB)

            encrypter = Encrypter(block_size, cipher)

            encrypted_text = encrypter.encode(plain_text)
            plain_text = encrypter.decode(encrypted_text)

            print(f'\nPlain text:\t\t\t\t{plain_text}\n'
                  f'Encrypted text:\t\t\t{encrypted_text}\n'
                  f'Encryption mode:\t\tECB\n'
                  f'Key size:\t\t\t\t{key_size*8}\n'
                  f'Block size:\t\t\t\t{block_size*8}\n'
                  f'Indent method:\t\t\tPKCS7\n'
                  f'Available key sizes:\t{tuple(i*8 for i in AES.key_size)}\n'
                  f'Available block size:\t{block_size*8}\n')
        elif choice == 2:
            print("Algorithms to compare: ГОСТ Р 34.12-2015 ('Кузнечик') и Rijndael.\n"
                  f"{'-'*58}\n"
                  f"| {'Key size':^23s} | {'256':^10s} | {'128, 192, 256':^15s} |\n"
                  f"{'-'*58}\n"
                  f"| {'Block size':^23s} | {'128':^10s} | {'128, 192, 256':^15s} |\n"
                  f"{'-'*58}\n"
                  f"| {'Amount of rounds':^23s} | {'10':^10s} | {'10, 12, 14':^15s} |\n"
                  f"{'-'*58}\n"
                  f"| {'Amount of subkeys':^23s} | {'10':^10s} | {'44-120 : 4':^15s} |\n"
                  f"{'-'*58}\n"
                  f"| {'Amount of S-blocks':^23s} | {'1':^10s} | {'2':^15s} |\n"
                  f"{'-'*58}\n"
                  f"| {'Publication year':^23s} | {'2015':^10s} | {'2001':^15s} |\n"
                  f"{'-'*58}\n"
                  f"| {'Suitable for protection':^23s} | {'Yes':^10s} | {'Yes':^15s} |\n"
                  f"{'-'*58}\n")
        elif choice == 0:
            print('Bye')
            break
