import json
import os

# Load library from file
def load_library(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library, filename):
    with open(filename, "w") as file:
        json.dump(library, file)

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the title/author: ").lower()
    print("Matching Books:")
    found = False
    for i, book in enumerate(library, 1):
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
            found = True
    if not found:
        print("No matching books found.\n")

# Display all books
def display_all_books(library):
    if not library:
        print("Library is empty.\n")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    print()

# Display statistics
def display_stats(library):
    total = len(library)
    read_count = sum(1 for book in library if book['read'])
    percentage = (read_count / total * 100) if total > 0 else 0
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%\n")

# Menu system
def main():
    filename = "library.txt"
    library = load_library(filename)

    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library, filename)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
