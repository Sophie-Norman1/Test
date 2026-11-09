print("Hello World")

class Book:
    def __init__(self, book, isbn, author, ):
        self.book = book
        self.isbn = isbn
        self.author = author
        self.withdrawn = []

    def Take_out_book(self):
        if self.book not in self.withdrawn:
            self.withdrawn.append(self.book)
        print(self.withdrawn)

book1 = Book("LOTR", 123456789, "J.R.R. Tolkein")
book1.Take_out_book()