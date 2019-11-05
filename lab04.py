try:
    from lab03 import Encrypter
except ModuleNotFoundError:
    print('You don\'t have lab03 package in your working directory')
    exit()


class BlEncr:
    def __init__(self, plain_text, code):
        self.plain_text = plain_text
        self.bin_code = bin(code)
        self.storage = []

    def operate(self, nonce):
        if len(self.plain_text) != len(nonce):
            raise AttributeError('\nnonce and plain_text have to have the same length\n')

        for index, letter in enumerate(self.plain_text):
            value = bin(nonce[index])
            encrypter = Encrypter(value, self.bin_code)

            encrypted_block = encrypter.operate()
            cipher_text = bin(int(encrypted_block, 2) ^ ord(letter))

            self.storage.append(encrypter._normalize_bin(bin_str=cipher_text, bin_len=8))

        return self.storage


def parse_bin_to_str(bin_str):
    parsed_string = ''

    while len(bin_str) > 0:
        parsed_string += chr(int(bin_str[0:8], 2))
        bin_str = bin_str[8:]

    return parsed_string


if __name__ == '__main__':

    while True:
        while True:
            try:
                choice = int(input('\nWhat to do:\n'
                                   '\t1 - encrypt\n'
                                   '\t2 - decrypt\n'
                                   '\t0 - exit\n'
                                   'Your choice: '))
                break
            except ValueError:
                print('\nYou have to input integer values\n')

        if choice < 0 or choice > 2:
            print('\nYour choice is out of range\n')
            continue
        elif choice == 0:
            print('Bye')
            break

        nonce = list(map(int, input('\nEnter the nonce:\t ').split()))

        while True:
            try:
                code = int(input('Enter the code:\t\t '))
                plain_text = input('Enter the open text: ')

                break

            except ValueError:
                print('\nFollow the instructions\n')
                continue

        bl_encr = BlEncr(plain_text, code)
        print(parse_bin_to_str(''.join(bl_encr.operate(nonce))))
