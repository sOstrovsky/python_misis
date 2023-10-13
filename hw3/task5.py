alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
shift = 4


def get_caesar_code(s):
    decoded = ''
    for i in s:
        if i.lower() in alphabet:
            idx = alphabet.index(i.lower())
            upd = idx + shift
            if upd > len(alphabet) - 1:
                decoded += alphabet[upd % len(alphabet)]
            else:
                decoded += alphabet[upd]
        else:
            decoded += i
    return decoded


def encode_caesar(s):
    encoded = ''
    for i in s:
        if i.lower() in alphabet:
            idx = alphabet.index(i.lower())
            upd = idx - shift
            if upd < 0:
                encoded += list(reversed(alphabet))[abs(upd) - 1]
            else:
                encoded += alphabet[upd]
        else:
            encoded += i
    return encoded


def print_result():
    s = input('Введите строку: ')
    decoded = get_caesar_code(s)
    print(f'Зашифрованная строка: {decoded}')
    encoded = encode_caesar(decoded)
    print(f'Расшифрованная строка: {encoded}')
