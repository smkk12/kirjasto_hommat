import argparse
import sys


class Book:
    def __init__(self, book_name, author, isbn, publish_year):
        self.book_name = book_name
        self.author = author
        self.isbn = isbn
        self.publish_year = publish_year

    def __str__(self):
        return f'{self.book_name}/{self.author}/{self.isbn}/{self.publish_year}'

class Library:
    def __init__(self,file_name):
        self.file_name = file_name
        print(f'Library initialized with file: {self.file_name}')

    def read_library_database(self):
        self.sort_library()
        try:
            with open(self.file_name) as file:
                current_database = file.read()
                print(f'~~~~~~~~~~~~~~ Current database: ~~~~~~~~~~~~~~\n{current_database}')
                print('~~~~~~~~~~~~~~ Current database ~~~~~~~~~~~~~~')
        except FileNotFoundError:
            print(f"File {self.file_name} not found.")

    def main_menu(self):
        while True:
            print('===MENU===')
            print('What would you like to do:')
            print('1. Add new book\n2. Print current Database\n3. Exit program')
            print('===MENU===')

            activity = input('Enter choice: ').strip()

            if activity == '1':
                self.add_new_book()

            elif activity == '2':
                self.read_library_database()

            elif activity == '3':
                print('Exiting program.')
                sys.exit() 
            else:
                print(f'Not a valid option: {activity}')

    def add_new_book(self):
        book_name = input('Insert book name: ').strip()
        author = input('Insert writers name: ').strip()
        isbn = input('Insert ISBN: ').strip()
        while True:
            publish_year_input = input('Enter publish year: ').strip()
            try:
                publish_year = int(publish_year_input)
                break  
            except ValueError:
                print('Publish year needs to be a number')

        book = Book(book_name,author,isbn,publish_year)
        print(f'Would you like to add following book to library (yes/no): {book}')

        while True:
            save = input('Save book? (yes/no): ').strip().lower()

            if save == 'yes':
                self.save_to_file(str(book))
                break
            elif save == 'no':
                print('Book not saved')
                break
            else:
                print('Invalid input. Please enter "yes" or "no".')

    def save_to_file(self,book,):
        with open (self.file_name,'a') as f:
            f.write(book+'\n')
            print(f'Book: {book},saved to library!')
            self.sort_library()

    def sort_library(self):
        with open(self.file_name, 'r') as file:
            lines = [line.strip() for line in file]
            lines.sort(key=lambda x: int(x.split('/')[-1]))

            with open(self.file_name, 'w') as file:
                for line in lines:
                    file.write(line + '\n')

def main():
    parser = argparse.ArgumentParser(description='Use "--file_name=<your text file here>" to start the program')
    parser.add_argument('--file_name', type=str, help='Insert your database text file',required=True)
    args = parser.parse_args()
    lib = Library(args.file_name)
    lib.main_menu()

if __name__ == '__main__':
    main()
