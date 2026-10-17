#Определяет язык текста (русский или английский).
def detect_language(text):

    for char in text.lower():
        # Проверяем на наличие русских букв
        if 'а' <= char <= 'я' or char == 'ё':
            return 'рус'
        # Проверяем на наличие английских букв
        elif 'a' <= char <= 'z':
            return 'англ'
    return 'англ'  # По умолчанию английский, если нет букв


#Шифрует или дешифрует текст с помощью шифра Цезаря.
def caesar_cipher(mode='шифрование'):

    #Просим пользователя ввести входные данные.
    text = input('Введите предложение.')
    shift = int(input('Введите значение сдвига.'))
    mode = input('Введите режим (шифрование / дешифрование).')

    # Определяем язык текста
    lang = detect_language(text)

    # Задаем алфавиты в зависимости от языка
    if lang == 'рус':
        alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        alphabet_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        alphabet_len = 33
    else:
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet_len = 26

    # Если режим дешифровки, инвертируем сдвиг
    if mode == 'дешифрование':
        shift = -shift

    result = ''

    # Проходим циклом по каждому символу в тексте
    for char in text:
        if char in alphabet_lower:
            index = alphabet_lower.find(char)
            new_index = (index + shift) % alphabet_len
            result += alphabet_lower[new_index]
        elif char in alphabet_upper:
            index = alphabet_upper.find(char)
            new_index = (index + shift) % alphabet_len
            result += alphabet_upper[new_index]
        else:
            # Знаки препинания, пробелы и цифры остаются без изменений
            result += char

    print(result)

caesar_cipher()
