import random

# Наборы символов.
lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers_chars = '0123456789'
special_chars = '!@#$%^&*()-_=+[]{};:,.<>?/'


# Генерация пароля.
def generate_password():

    # Пользователю нужно выбрать параметры.
    length = int(input('Введите длину пароля.'))
    lowercase = input('Использовать нижний регистр? (да/нет)')
    uppercase = input('Использовать верхний регистр? (да/нет)')
    numbers = input('Использовать цифры? (да/нет)')
    special = input('Использовать специальные символы? (да/нет)')

    # Собираем пул символов по настройкам.
    pool = ''
    if lowercase == "да":
        pool += lowercase_chars
    if uppercase == "да":
        pool += uppercase_chars
    if numbers == "да":
        pool += numbers_chars
    if special == "да":
        pool += special_chars

    # Если ни один тип символов не выбран — ошибка.
    if pool == '':
        return 'Ошибка: выберите хотя бы один тип символов!'

    # Генерируем пароль.
    password = ''
    for _ in range(length):
        password += random.choice(pool)
    print(password)

generate_password()