# library_manager.py
# Library Inventory and Checkout Manager
# Author: Ahmet
# Note* I used AI to help plan the structure/pseudocode, but I typed, reviewed, and understand the final code myself.

from datetime import date, timedelta
from library_books import library_books # starter list of book dictionaries

# Work directly with the starter list from library_books.py
books = library_books

def view_available_books():
    """Level 1: Print all available books (id, title, author)."""

    print("\nAvailable books:")
    found_any = False
    for book in books:
        if book["available"]:
            found_any = True
            print(f"{book['id']}: {book['title']} by {book['author']}")
    if not found_any:
        print("No books are currently available.")

def search_books():
    """
    Level 2:
    Case-insensitive search by author or genre.
    """
    term = input("Enter an author or genre to search: ").strip().lower()
    print(f"\nResults for '{term}':")
    found_any = False
    for book in books:
        author = book["author"].lower()
        genre = book["genre"].lower()
        if term in author or term in genre:
            found_any = True
            status = "Available" if book["available"] else f"Checked out (due {book['due_date']})"
            print(f"{book['id']}: {book['title']} by {book['author']} - {status}")
    if not found_any:
        print("No matching books found.")

def checkout_book():
    """
    Level 3:
    Checkout a book by ID.
    If available:
      - mark unavailable
      - set due_date to 2 weeks from today
      - increment checkouts
    Otherwise, show a message.
    """
    book_id = input("Enter the ID of the book to check out: ").strip()
    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                print("That book is already checked out.")
                return
            # Mark the book as checked out
            book["available"] = False
            # Set due date 2 weeks from today
            due = date.today() + timedelta(days=14)
            book["due_date"] = due.isoformat()
            # Increment checkout count
            book["checkouts"] += 1
            print(f"Checked out '{book['title']}'. Due on {book['due_date']}.")
            return
    print("No book found with that ID.")

def show_menu():
    """
    Simple text menu for the librarian to choose actions.
    """
    print("\nLibrary Manager - Menu")
    print("1. View available books")
    print("2. Search by author or genre")
    print("3. Checkout a book")
    print("4. Quit")
    return input("Choose an option (1-4): ").strip()

def main():
    """Main loop: keep showing the menu until the user quits."""
    print("Welcome to the library inventory and Checkout Manager.")
    while True:
        choice = show_menu()
        if choice == "1":
            view_available_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            checkout_book()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()