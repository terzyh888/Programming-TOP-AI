"""Калькулятор на базе NumPy.

Этот модуль запрашивает у пользователя два числа и выбранную операцию,
после чего производит вычисление с использованием функций NumPy.
"""

import numpy as np


def calculate() -> None:  #Запрашивает у пользователя два числа и операцию, а затем выводит результат.
    print("--- Простой калькулятор ---")

    # Получаем числа от пользователя
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: пожалуйста, вводите только числа.")
        return

    # Выбор операции
    print("Сложение (+)")
    print("Вычитание (-)")
    print("Умножение (*)")
    print("Деление (/)")

    choice = input("Выберите операцию: ")

    # Вычисления с помощью numpy
    if choice == "+":
        result = np.add(num1, num2)
        print(f"Результат: {num1} + {num2} = {result}")
    elif choice == "-":
        result = np.subtract(num1, num2)
        print(f"Результат: {num1} - {num2} = {result}")
    elif choice == "*":
        result = np.multiply(num1, num2)
        print(f"Результат: {num1} * {num2} = {result}")
    elif choice == "/":
        if num2 == 0:
            print("Ошибка: деление на ноль невозможно.")
            return
        result = np.divide(num1, num2)
        print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Ошибка: неверный выбор операции.")


if __name__ == "__main__":
    calculate()