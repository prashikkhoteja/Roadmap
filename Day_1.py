class Library:
    def __init__(self):
        self.book = {}

    def add_book(self):
        a = int(input("Enter the number of books you want to add:"))
        print(f"Enter the name of {a} books: ")
        for n in range(a):
            book_name = input(f"Book No {n+1}: ")
            self.book[book_name] = "available"
            print(f"{book_name} added successfully.")

    def search_book(self):
        search = input("Enter the book you want to look for: ")
        if search in self.book:
            print(f"{search} is available.")
        else:
            print(f"{search} is not available.")

    def display_book(self):
        print(f"{self.book}")

    def remove_book(self):
        unwanted = input("Enter the name of the book you want to remove:")
        if unwanted in self.book:
            del self.book[unwanted]
            print("Book deleted")
        else:
            print("Invalid, Book Not Found. ")


my_library = Library()

while True:
    print("\nType 1 To Add book.")
    print("Type 2 To Search Book.")
    print("Type 3 To Display Book.")
    print("Type 4 To Remove Book.")
    print("Type 5 to exit.")
    print("\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        my_library.add_book()
    elif choice == 2:
        my_library.search_book()
    elif choice == 3:
        my_library.display_book()
    elif choice == 4:
        my_library.remove_book()
    elif choice == 5:
        break
