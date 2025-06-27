# Section 1, Q2: OOP Implementation – Library Management

class Person:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        
        print(f"Person: {self.name}")


class User(Person):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = []

    def display_info(self):
        # Method overriding
        print(f"Library User: {self.name}")

    def view_books(self, library):
        print("\nCurrent Library Collection:")
        library.list_books()

    def borrow_book(self, title, library):
        book = library.find_book(title)
        if not book:
            print(f"  ➔ Book '{title}' not found.")
        elif not book.available:
            print(f"  ➔ '{title}' is already checked out.")
        else:
            book.available = False
            self.borrowed_books.append(book)
            print(f"  ➔ You have borrowed '{title}'.")

    def return_book(self, title, library):
        for book in self.borrowed_books:
            if book.title.lower() == title.lower():
                book.available = True
                self.borrowed_books.remove(book)
                print(f"  ➔ You have returned '{title}'.")
                return
        print(f"  ➔ You did not borrow '{title}'.")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"{self.title} by {self.author} — {status}"


class Library:
     def __init__(self):
        self.collection = []

     def add_book(self, book):
        self.collection.append(book)

     def list_books(self):
         if not self.collection:
            print("  (no books in library)")
         for book in self.collection:
            print(f"  - {book}")

     def find_book(self, title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                return book
        return None


def main():
    
       library = Library()
       library.add_book(Book("1984", "George Orwell"))
       library.add_book(Book("Dune", "Frank Herbert"))
       library.add_book(Book("Harry Potter", "J.K. Rowling"))

 
       user = User("Alice")

       print("Welcome to the Library Management System")
       user.display_info()
       while True:

          print("""
Please choose an action:
  1) View all books
  2) Borrow a book
  3) Return a book
  4) Exit
""")
          choice = input("Enter choice (1–4): ").strip()
          if choice == "1":
             user.view_books(library)
          elif choice == "2":
            title = input("Enter the title you want to borrow: ").strip()
            user.borrow_book(title, library)
          elif choice == "3":
            title = input("Enter the title you want to return: ").strip()
            user.return_book(title, library)
          elif choice == "4":
            print("Goodbye!")
            break
          else:
              print("Invalid selection; please choose 1–4.")

if __name__ == "__main__":
    main()

