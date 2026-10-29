class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def info(self):
        return f"книга - {self.title}, автор - {self.author}, год - {self.year}"

class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"книга - {self.title}, автор - {self.author}, год - {self.year}, формат - {self.format}"

book_cats = Book("Путешествия котов", "Лорд де Кот", 2000)
ebook_dogs = Ebook("Путешествия собачек", "Барон Догвиль", 2001, "электронный")

print(book_cats.info())
print(ebook_dogs.info())