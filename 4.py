from abc import ABC, abstractmethod
import datetime


# 1. Создаем абстрактный класс Printable с абстрактным методом print_info()
class Printable(ABC):
    @abstractmethod
    def print_info(self):
        print(f"Печать информации: {self.info()}")


class Book(Printable):  # 2. Реализуем абстрактный класс в классе Book
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"книга - {self.title}, автор - {self.author}, год - {self.year}"

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title

    @property
    def age(self):
        # Исправлено обращение к datetime (datetime.datetime.now())
        return datetime.datetime.now().year - self.year

    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(";")
        return cls(title, author, int(year))

    # Реализация абстрактного метода из Printable
    def print_info(self):
        print(self.info())


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"книга - {self.title}, автор - {self.author}, год - {self.year}, формат - {self.format}"

    def __str__(self):
        return self.info()


# Проверка работы
book_cats = Book("Путешествия котов", "Лорд де Кот", 2000)
ebook_dogs = Ebook("Путешествия собачек", "Барон Догвиль", 2001, "электронный")

print(book_cats.info())
print(ebook_dogs.info())

# Проверка вызова метода print_info из абстрактного класса
book_cats.print_info()