import art as a


# Продублировали алфавит для того, чтобы осуществить сдвиг буквы Z
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 1]


# Мой вариант реализации шифра Цезаря
def encrypt1(plain_text, shift_amount):
    # Ищем положение кодируемой буквы в введенном слове
    for pos_text in range(len(plain_text)):
        # Ищем букву в алфавите
        if plain_text[pos_text] in alphabet:
            # Если находим, то сохраняем в переменной
            letter = plain_text[pos_text]
            # Ищем положение этой буквы в алфавите
            for pos_alphabet in range(len(alphabet)):
                # Сравниваем буквы в алфавите и слове
                if letter == alphabet[pos_alphabet]:
                    # Если они равны, то заменяем на букву со определенным сдвигом
                    encrypt_word = plain_text.replace(plain_text[pos_text], alphabet[pos_alphabet + shift_amount])
                    # Собираем буквы в ряд
                    print(encrypt_word[pos_text], end='')


# Реализация из курса
def encrypt2(plain_text, shift_amount):
    # Создаем перменную для помещения в неё кодируемых букв
    encrypt_text = ''
    # Перебираем буквы в слове
    for letter in plain_text:
        # Ищем позицию буквы в алфавите
        index = alphabet.index(letter)
        # Определяем новый индекс относительно сдвига
        new_index = index + shift_amount
        # Определяем новую букву из алфавита с новым индексом
        encrypt_text += alphabet[new_index]
    print(encrypt_text)


def encode(plain_text, shift_amount):
    encode_text = ''
    for letter in plain_text:
        index = alphabet.index(letter)
        new_index = index - shift_amount
        encode_text += alphabet[new_index]
    print(encode_text)


# Объединение шифрования и дешифрования в одну функцию
def caesar(plain_text, shift_amount, cipher_direction):
    new_text = ''
    if direction == 'decode':
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + shift_amount
            new_text += alphabet[new_index]
        else:
            new_text += letter
    print(f'Your {cipher_direction} text: {new_text}')


print(a.logo)


Flag = True
while Flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = str(input("Type your message:\n")).lower()
    shift = int(input("Type the shift number:\n"))


shift = shift % 25
caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)


result = input("You want to restart the cipher program? Yes or No\n").lower()
if result == 'no':
    Flag = False
    print("Goodbye")
