import unittest


class BoolReaderSystem():
    def __init__(self, books):
        self.__userManeger = UserManeger
        self.__library = Library(books)

    def addUser(self, user):
        self.__userManeger.addUser(user)

    def addBook(self, book):
        self.__library.addBook(book)

    def getBook(self, book, user):
        return self.__library.getBook(book, user)

    def returnBook(self, book, user):
        return self.__library.returnBook(book, user)


class User():
    def __init__(self, ID):
        self.__id = ID
        self.havingBook = None

    def getID(self):
        return self.__id


class UserManeger():
    def __init__(self):
        self.__userMaps = {}

    def addUser(self, user):
        self.__userMaps[user.getID()] = user


class Book():
    def __init__(self, ID):
        self.__id = ID
        self.rentingUser = None
        self.isRented = False

    def getID(self):
        return self.__id


class Library():
    def __init__(self, books=None):
        self.__bookMaps = {}
        for book in books:
            self.__bookMaps[book.getID()] = book

    def addBool(self, book):
        self.__bookMaps[book.getID()] = book

    def getBook(self, book, user):
        if self.__bookMaps[book.getID()].isRented == True:
            return "Occupied !!!"
        self.__bookMaps[book.getID()].isRented = True
        user.havingBook = self.__bookMaps[book.getID()]
        self.__bookMaps[book.getID()].rentingUser = user

    def returnBook(self, book, user):
        self.__bookMaps[book.getID()].isRented = False
        self.__bookMaps[book.getID()].rentingUser.havingBook = None


class Test(unittest.TestCase):
    def test_book_reader(self):
        book1 = Book("One Peace")
        book2 = Book("Kimetu no Yaiba")

        reader = BoolReaderSystem([book1, book2])

        user1 = User("!")
        user2 = User("2")

        reader.getBook(book1, user1)
        reader.getBook(book2, user2)

        self.assertEqual(reader.getBook(book1, user1), "Occupied !!!")
        self.assertEqual(user1.havingBook, book1)

        reader.returnBook(book1, user1)

        self.assertEqual(user1.havingBook, None)


if __name__ == "__main__":
    unittest.main()
