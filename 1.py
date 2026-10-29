class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def info(self):
        return f"книга - {self.title}, автор - {self.author}, год - {self.year}"

book_cats = Book("Путешествия котов", "Лорд де Кот", 2000)
print(book_cats.info())