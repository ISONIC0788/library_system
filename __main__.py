from library_system.core import Book, Library
from library_system.utils import borrow_item

# A simple User class to simulate authentication/roles
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def main():
    print("===  Smart Library System Demo ===\n")

    # 1. Setup Users & Library
    admin = User("Alice", "Admin")
    guest = User("Bob", "Guest")
    my_library = Library()

    # 2. Create Books
    b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    b2 = Book("1984", "George Orwell", 328)
    b3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180) # Duplicate for equality test

    # 3. Test Permission Check (Closure)
    print("--- Testing Permissions ---")
    my_library.add_book(guest, b1)  # Should fail (Bob is Guest)
    my_library.add_book(admin, b1)  # Should succeed (Alice is Admin)
    my_library.add_book(admin, b2)

    # 4. Test Dunder Methods
    print("\n--- Testing Dunder Methods ---")
    print(f"String Rep (__str__): {b1}")
    print(f"Length (__len__): {len(b1)} pages")
    print(f"Equality (__eq__): b1 == b3 is {b1 == b3}") # True

    # 5. Test Iteration (__getitem__)
    print("\n--- Testing Iteration ---")
    print("Library contents:")
    for book in my_library:
        print(f" - {book}")

    # 6. Test Logging Decorator
    print("\n--- Testing Logging Decorator ---")
    my_library.borrow_book("1984")
    my_library.return_book("1984")

    # 7. Test Duck Typing
    print("\n--- Testing Duck Typing ---")
    
    # A dummy class that looks like a book but isn't one
    class Magazine:
        def __init__(self, title):
            self.title = title
            
    mag = Magazine("National Geographic")
    
    borrow_item(b1)   # Works (is a Book)
    borrow_item(mag)  # Works (has .title, so it quacks like a duck)
    borrow_item("Just a String") # Fails gracefully

if __name__ == "__main__":
    main()