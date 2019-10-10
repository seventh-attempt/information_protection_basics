class Encrypter:
    def __init__(self, alphabet, table):
        self.alphabet = alphabet
        self.table = table

    def encrypt(self, key, open_text):
        result = ''

        for i in range(len(open_text)):
            key_index, text_index = self.alphabet.find(key[i]), self.alphabet.find(open_text[i])
            result += self.table[key_index][text_index]

        return result
            
    def decrypt(self, key, encrypted_text):
        result = ''

        for i in range(len(encrypted_text)):
            key_index = self.alphabet.find(key[i])
            text_index = self.table[key_index].index(encrypted_text[i])

            result += self.alphabet[text_index]
    
        return result


def check_input(text, key, alphabet):
    if len(text) != len(key):
        print('\nKey and text must have the same length\n')
        return False

    if not all(i in alphabet for i in text) or \
                not all(i in alphabet for i in key):
        print('\nYou have to input only symbols from russian alphabet\n')
        return False

    return True


if __name__ == '__main__':
    alphabet = ''.join([chr(i) for i in range(ord('а'), ord('а')+32)])
    alphabet = alphabet[:6] + chr(1105) + alphabet[6:]
#    alphabet = ''.join([chr(i) for i in range(ord('a'), ord('a')+26)])
    table = []
    print(alphabet)

    for i in range(len(alphabet)):
        table.append(list(''.join((alphabet[i:], alphabet[:i]))))
    
    while True:
        while True:
            try:
                choice = int(input('What do you want to do:\n'
                                   + '\t1 - Encrypt phrase\n'
                                   + '\t2 - Decrypt phrase\n'
                                   + '\t3 - Print table\n'
                                   + '\t0 - Exit\n'
                                   + 'Your choice: '))
                break
            except ValueError:
                print('\nYou have to input integer number\n')

        encrypter = Encrypter(alphabet, table)
        
        if choice < 0 or choice > 3:
            print('\nThere\'s no such a choice\n')
        elif choice == 1:
            open_text = input('Enter text to encrypt: ')
            key = input('Enter encryption key:  ')

            if not check_input(open_text, key, alphabet):
                continue

            print(f'\ntext:   {open_text}')
            print(f'key:    {key}')
            print(f'result: {encrypter.encrypt(key, open_text)}\n')

        elif choice == 2:
            encrypted_text = input('Enter text to decrypt: ')
            key = input('Enter decryption key:  ')

            if not check_input(encrypted_text, key, alphabet):
                continue

            print(f'\ntext:   {encrypted_text}')
            print(f'key:    {key}')
            print(f'result: {encrypter.decrypt(key, encrypted_text)}\n')

        elif choice == 3:
            for i in table:
                print(i)
            input()

        if choice == 0:
            print('Bye')
            break

