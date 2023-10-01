origin = 'объектно-ориентированный'


def get_words():
    word1 = origin[:6]
    word2 = origin[9:17]
    word3 = origin[14:17]
    word4 = origin[4] + origin[7] + origin[14]
    word5 = origin[10] + origin[12: 15] + origin[19]
    return word1, word2, word3, word4, word5


def print_result():
    print(get_words())
