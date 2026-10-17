# Таблица соответствия римских и арабских цифр.
roman_numerals = {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
    'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
    'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
}


def convert(value):
    """Конвертирует число в обе стороны:
    - если передано int → возвращает римское число
    - если передана строка → возвращает арабское число"""

    # Если передано число — конвертируем в римское
    if isinstance(value, int):
        if value <= 0 or value > 3999:
            return 'Ошибка: число должно быть от 1 до 3999'
        result = ''
        for roman, num in roman_numerals.items():
            while value >= num:
                result += roman
                value -= num
        return result

    # Если передана строка — конвертируем в арабское
    if isinstance(value, str):
        roman = value.upper()
        total = 0
        i = 0
        for symbol, num in roman_numerals.items():
            while roman[i:i + len(symbol)] == symbol:
                total += num
                i += len(symbol)
                if i >= len(roman):
                    break
        if i < len(roman):
            return 'Ошибка: некорректное римское число'
        return total

    return 'Ошибка: поддерживаются только int и str'


# Тесты.
roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
int_tests = [4, 9, 42, 99, 2023]

print('Римские → обычные')
for roman in roman_tests:
    print(f'{roman} = {convert(roman)}')

print('\nОбычные → римские')
for num in int_tests:
    print(f'{num} = {convert(num)}')