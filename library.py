import json
from typing import List, Dict, Union

DATA_FILE = 'data.json'


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "in stock"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


class Library:
    def __init__(self):
        self.books = self.load_data()

    def load_data(self) -> List[Book]:
        try:
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                return [Book(**book) for book in data['books']]
        except FileNotFoundError:
            return []

    def save_data(self) -> None:
        with open(DATA_FILE, 'w') as file:
            json.dump({"books": [book.to_dict()
                      for book in self.books]}, file, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        new_id = len(self.books) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_data()
        print(f"Book '{title}' is added.")

    def delete_book(self, id: int) -> None:
        index = self.binary_search(id)
        if index != -1:
            del self.books[index]
            self.save_data()
            print(f"Book with ID {id} is deleted.")
        else:
            print(f"Book with ID {id} is not found.")

    def search_books(self, query: Union[str, int], by: str = 'title') -> List[Book]:
        '''Used Union because books can be searched by title, author or
            year, id, which are string and int types respectfully.'''
        result = []
        for book in self.books:
            if str(getattr(book, by)).lower() == str(query).lower():
                result.append(book)
        return result

    def display_books(self) -> None:
        for book in self.books:
            print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")

    def update_book_status(self, id: int, status: str) -> None:
        index = self.binary_search(id)
        if index != -1:
            self.books[index].status = status
            self.save_data()
            print(f"Book's status with id {id} is updated to '{status}'.")
        else:
            print(f"Book with ID {id} is not found.")

    def binary_search(self, id):
        low = 0
        high = len(self.books) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.books[mid].id == id:
                return mid
            elif self.books[mid].id < id:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
