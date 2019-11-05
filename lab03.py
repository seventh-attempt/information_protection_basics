class Encrypter:

    def __init__(self, letter, bin_key):
        self.letter = letter
        self.bin_key = self._normalize_bin(bin_key)

    @staticmethod
    def _normalize_bin(bin_str, bin_len=10):
        bin_str = bin_str[2:]
        key_len = len(bin_str)

        if key_len < bin_len:
            return '0' * (bin_len-key_len) + bin_str
        else:
            return bin_str

    @staticmethod
    def _left_shift(key, num=1):
        return key[num:5] + key[0:num] + key[5+num:] + key[5:5+num]

    @staticmethod
    def _shuffle_key(key, pattern=(6, 3, 7, 4, 8, 5, 10, 9)):
        shuffled_key = ''

        for position in pattern:
            shuffled_key += key[position-1]

        return shuffled_key

    def _get_keys(self):
        key = self._shuffle_key(self.bin_key, pattern=(3, 5, 2, 7, 4, 10, 1, 9, 8, 6))

        key = self._left_shift(key)
        key1 = self._shuffle_key(key)
        key = self._left_shift(key, num=2)
        key2 = self._shuffle_key(key)

        return key1, key2

    def _operation2(self, key_l, key_r, key):
        er_p = int(self._shuffle_key(key_r, pattern=(4, 1, 2, 3, 2, 3, 4, 1)), 2)
        key = int(key, 2)

        xor = self._normalize_bin(bin(er_p ^ key), bin_len=8)
        xor_l, xor_r = xor[:4], xor[4:]

        s_l = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 1]]
        s_r = [[1, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

        l = self._normalize_bin(
            bin(s_l[int(xor_l[0]+xor_l[3], 2)][int(xor_l[1:3], 2)]), bin_len=2
        )
        r = self._normalize_bin(
            bin(s_r[int(xor_r[0]+xor_r[3], 2)][int(xor_r[1:3], 2)]), bin_len=2
        )

        seq = l + r
        p4 = self._shuffle_key(seq, pattern=(2, 4, 3, 1))

        return self._normalize_bin(bin(int(key_l, 2) ^ int(p4, 2)), bin_len=4)

    def operate(self, operation='encryption'):
        if operation == 'encryption':
            key1, key2 = self._get_keys()
        elif operation == 'decryption':
            key2, key1 = self._get_keys()
        else:
            return f'Operation {operation} doesn\'t exist'

        letter_code = self._normalize_bin(self.letter, bin_len=8)

        IP = self._shuffle_key(letter_code, pattern=(2, 6, 3, 1, 4, 8, 5, 7))
        L, R = IP[:4], IP[4:]

        op2 = self._operation2(L, R, key1)
        op3_1 = R + op2
        L, R = op3_1[:4], op3_1[4:]
        op4 = self._operation2(L, R, key2)

        return self._shuffle_key(op4 + R, pattern=(4, 1, 3, 5, 7, 2, 8, 6))


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

        operation = 'encryption'

        if choice < 0 or choice > 2:
            print('\nYour choice is out of range\n')
            continue
        elif choice == 2:
            operation = 'decryption'
        elif choice == 0:
            print('Bye')
            break

        try:
            letter = input('\nEnter the letter: ')
            key = int(input('Enter the key:    '))
        except ValueError:
            print('\nFollow the instructions!!!\n')
            continue

        bin_key = bin(key)
        full_letter_code = bin(ord(letter))

        encrypter = Encrypter(full_letter_code, bin_key)

        print(f'result: {chr(int(encrypter.operate(operation), 2))}')
