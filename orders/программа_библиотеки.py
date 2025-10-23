class LibrarySystem:
    def __init__(self):
        self.books ={}

    def add_book(self, isbn, title, author, year):
        if isbn not in self.books:
            self.books[isbn] = {'title':title, 'author':author, 'year':year}
            print(f'Book {title} by {author} added to the library.')
        else:
            print(f'Book with this ISBN already exists in the library.')

    def change_status(self, isbn, status):
        if isbn not in self.books:
            self.books[isbn]['status'] = status
            print(f'Status of book {self.books[isbn]["title"]} changed to {status}.')
        else:
            print(f'Book with this ISBN doesnt es exist in the library.')

    def search_book(self, isbn):
        if isbn in self.books:
            book_info = self.books[isbn]
            print(
                f"ISBN: {isbn}\nTitle: {book_info['title']}\nAuthor: {book_info['author']}\nYear: {book_info['year']}\nStatus: {book_info['status']}")
        else:
            print("Book with this ISBN doesn't exist in the library.")


#С ОПИСАНИЕМ
class Library:
    def __init__(self):
        self.books = {}  #инициализация словаря для хранения информации о книгах

    def add_book(self, isbn, title, author, year):
        #метод для добавления книги в систему. принимает ISBN, название, автора и год выпуска
        if isbn not in self.books:
            #если книги с таким ISBN нет в системе, добавляем ее
            self.books[isbn] = {'title': title, 'author': author, 'year': year, 'status': 'available'}
            print(f"Book {title} by {author} added to the library.")
        else:
            #если книга с таким ISBN уже существует, выводим сообщение
            print("Book with this ISBN already exists in the library.")

    def change_status(self, isbn, status):
        #метод для изменения статуса книги. принимает ISBN и новый статус
        if isbn in self.books:
            #если книга с таким ISBN найдена, обновляем ее статус
            self.books[isbn]['status'] = status
            print(f"Status of book {self.books[isbn]['title']} changed to {status}.")
        else:
            #если книга с таким ISBN не найдена, выводим сообщение
            print("Book with this ISBN doesn't exist in the library.")

    def search_book(self, isbn):
        #метод для поиска книги по ISBN. выводит информацию о книге или сообщение, если книга не найдена
        if isbn in self.books:
            book_info = self.books[isbn]
            print(f"ISBN: {isbn}\nTitle: {book_info['title']}\nAuthor: {book_info['author']}\nYear: {book_info['year']}\nStatus: {book_info['status']}")
        else:
            print("Book with this ISBN doesn't exist in the library.")