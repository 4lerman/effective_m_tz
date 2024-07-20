from library import Library


def main():
    library = Library()
    while True:
        print("\nLibrary management system")
        print("1. Add book")
        print("2. Delete book")
        print("3. Search books")
        print("4. List all books")
        print("5. Change book status")
        print("6. Exit")
        choice = input("Choose action: ")

        if choice == '1':
            title = input("Input book title: ")
            author = input("Input book author: ")
            year = int(input("Input book published year: "))
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Give book id to remove it: "))
            library.delete_book(book_id)
        elif choice == '3':
            by = input("Search by (title/author/year/id): ")
            query = input("Input search query: ")
            if by == 'year':
                query = int(query)  # Преобразовать в int для поиска по году
            results = library.search_books(query, by)
            for book in results:
                print(
                    f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
        
        elif choice == '4':
            library.display_books()

        elif choice == '5':
            book_id = int(input("Input book id: "))
            status = input("Input new status (in stock/given): ")
            library.update_book_status(book_id, status)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
