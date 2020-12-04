class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvialableBooks(self):
        print("The avialable books in library are: ")
        with open("Books.txt") as f:
            BookData = f.read()
            print(BookData)
            f.close()

    def borrowBook(self, bookName):
        with open("Books.txt") as f:
            data = f.read()
        if bookName in data:
            print(f"You have been issued this book: {bookName}")
            print(f"Please return the book within 30 days, Thank You !!!!")
            with open("Books.txt", "r") as f:
                lines = f.readlines()
            with open("Books.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != bookName:
                        f.write(line)
            f.close()
            return True
        else:
            print(f"The book {bookName} is not available currently")
            return False

    def returnBook(self, bookName):
        with open("Books.txt", "a") as f:
            f.write(bookName + '\n')
            f.close()
        print(f"Your book {bookName} is returned successfully, Thanks Come Again!!!!")

    def addBook(self, bookName):
        with open("Books.txt", "a") as f:
            f.write(bookName + '\n')
            f.close()
        print("Your book is successfully added to the library !!!!")

    def removeBook(self, bookName):
        with open("Books.txt", "r") as f:
            lines = f.readlines()
        with open("Books.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != bookName:
                    f.write(line)
        f.close()
        print("Your book is successfully removed from the library")


class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book you want: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    with open("Books.txt") as f:
        data = f.read()
    centralLib = Library(data)
    student = Student()
    while True:

        message = '''***********Welcome to the Central Library***********
        
        ll        ii  bbbb    rrrrr    aaaaa   rrrrr    y     y
        ll        ii  b   b   r    r   a   a   r    r    y   y
        ll        ii  bbbb    rrrrr    aaaaa   rrrrr      yy
        ll        ii  b   b   rr       a   a   rr         yy
        lllllll   ii  bbbb    r rrr    a   a   r rrr      yy
         
        
        Please choose any option:
        1. List of all the Books available
        2. Borrow a Book
        3. Return a Book
        4. Add a Book
        5. Remove a Book
        6. Exit the library
        '''
        print(message)
        a = int(input("Enter any choice: "))

        if a == 1:
            centralLib.displayAvialableBooks()
        elif a == 2:
            centralLib.borrowBook(student.requestBook())
        elif a == 3:
            centralLib.returnBook(student.returnBook())
        elif a == 4:
            k = input("Enter the book you want to add: ")
            centralLib.addBook(k)
        elif a == 5:
            m = input("Enter the book you want to remove: ")
            centralLib.addBook(m)
        elif a == 6:
            print("Thanks for using the library, Please come again Have a nice day!!!")
            exit()
        else:
            print("!!!!!Invalid Choice!!!!!")
