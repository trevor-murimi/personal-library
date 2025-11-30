# The main list that will hold all our book dictionaries
Library = []

# function to add a new book to the library


def add_book():
    print("\n--- Add new book ---")
    title = input("Enter the title: ").strip()
    author = input("Enter the author: ").strip()

    year_str = input("Enter the publication year: ").strip()
    year = int(year_str)

    pages_str = input("Enter total pages: ").strip()
    pages = int(pages_str)

    rating_str = input("Enter your rating (1.0 to 5.0): ").strip()
    rating = float(rating_str)

    read_input = input("Have you read the book? (yes/no): ").strip().lower()
    read = True if read_input == 'yes' else False

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'pages': pages,
        'rating': rating,
        'read': read,
    }

    Library.append(new_book)
    print(f"Book '{title}' by {author} added to the library.")

# function to list all books in the library


def list_book():
    print("\n--- Your current library ---")
    if not Library:
        print("Your library is empty. Add some books.")
        return

    for book in Library:
        read_status = "✅ READ" if book['read'] else "❌ NOT READ"
        print(f"  Title: {book['title']}")
        print(f"  Author: {book['author']}")
        print(f"  Year: {book['year']}")
        print(f"  Pages: {book['pages']}")
        print(f"  Rating: {book['rating']:.1f}")
        print(f"  Status: {read_status}")
        print("-" * 20)

# function to find a book by title


def find_book():
    print("\n--- Find book by title ---")
    if not Library:
        print("Your library is empty.")
        return

    search_title = input(
        "Enter the title of the book to find: ").strip().lower()
    found = False

    for book in Library:
        # compare normalized titles
        if book['title'].strip().lower() == search_title:
            read_status = "✅ READ" if book['read'] else "❌ NOT READ"
            print("\n**Book Found!**")
            print(f"  Title: {book['title']}")
            print(f"  Author: {book['author']}")
            print(f"  Year: {book['year']}")
            print(f"  Pages: {book['pages']}")
            print(f"  Rating: {book['rating']:.1f}")
            print(f"  Status: {read_status}")
            found = True
            break

    # <-- correct place: after the for-loop
    if not found:
        print(f"Book with title '{search_title}' not found.")

# function to get library statistics


def get_stat():
    print("\n--- Library ststistics ---")
    # the number of books is the length of the Library list
    total_books = len(Library)
    if total_books == 0:
        print("No book to calculate statistics")
        return
    # initialize variables for calculations
    total_rating = 0.0  # initialize as a float

    # iterate through the list and accumulate the rating
    for book in Library:
        # The rating value is a float so adding it accumulates a float sum
        total_rating += book['rating']

    # calculate the average rating
    average_rating = total_rating / total_books

    # output the results
    print(f"Total books in library: {total_books}")
    print(f"Total cumulative rating: {total_rating:.1f}")
    # We use {:.2f} to display the average with two decimal places (Float)
    print(f"Average book rating: {average_rating:.2f}")

# --- Main Program Loop ---


def main():
    while True:
        print("\n--- Personal Library Manager ---")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Find book by title")
        print("4. Get library statistics")
        print("5. Exit")
        choice = input("Enter your choice (1,2,3,4 or 5 ) ").strip()
        if choice == '1':
            add_book()
        elif choice == '2':
            list_book()
        elif choice == '3':
            find_book()
        elif choice == '4':
            get_stat()
        elif choice == '5':
            print("Thank you for using the library manager. Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, 3 or 4")


if __name__ == "__main__":
    main()
