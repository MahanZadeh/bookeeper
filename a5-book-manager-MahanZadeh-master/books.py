import json
from os import path
import xlrd


class Book:

    def __init__(self, author: str, title: str, publisher: str, shelf, category: str, subject: str):
        """Create a new Book object and initialize attributes.

        :param author: a string
        :param title: a string
        :param publisher: a string
        :param shelf: a string or a positive number
        :param category: a string
        :param subject: a string
        :precondition author: a string specifying the author of the book
        :precondition title: a string specifying the title of the book
        :precondition publisher: a string specifying the publisher of the book
        :precondition shelf: a string specifying the person or location of the book (e.g., "on my desk", "student") or
        a positive number, specifying the shelf number
        :precondition category: a string specifying the category of the book
        :precondition subject: a string specifying the subject of the book
        :postcondition: correctly creates a Book object with the specified attributes

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> book_one
        Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)
        >>> book_one.author
        'Mahan'
        >>> book_one.shelf
        '1'
        """
        self.author = author
        self.title = title
        self.publisher = publisher
        self.shelf = shelf
        self.category = category
        self.subject = subject

    def change_shelf(self, new_shelf_number):
        """Change the shelf attribute of the book.

        :param new_shelf_number: a string or a positive number
        :precondition: a string specifying the person or location of the book (e.g., "on my desk", "student") or
        a positive number, specifying the shelf number
        :postcondition: correctly changes the shelf attribute of the book to the specified new_shelf_number
        :return: the book with the updated shelf attribute

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> book_one.change_shelf(2)
        Book(Mahan, Tears in the time of Corona, Independent, 2, Life, Slice of Life)
        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> book_one.change_shelf("student")
        Book(Mahan, Tears in the time of Corona, Independent, student, Life, Slice of Life)
        """
        self.shelf = new_shelf_number
        return self

    def __repr__(self):
        """Provide the attributes of the Book object.

        :return: the attributes of the Book object

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> book_one
        Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)
        """
        return f'Book({self.author}, {self.title}, {self.publisher}, {self.shelf}, {self.category}, {self.subject})'

    def __str__(self):
        """Provide the information of the Book object.

        :return: the information of the Book object

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> print(book_one)
        Title: 'Tears in the time of Corona', Author: 'Mahan', Publisher: 'Independent', Category: 'Life', Subject: 'Slice of Life', Shelf: '1'
        """
        return f"Title: '{self.title}', Author: '{self.author}', Publisher: '{self.publisher}', Category: " \
               f"'{self.category}', Subject: '{self.subject}', Shelf: '{self.shelf}'"


class Library:

    def __init__(self):
        """Create a library object that contains an empty list.

        :postcondition: creates a library object with an empty list inside of it
        """
        self.libraries = []

    def add_books(self, book_object):
        """Add the specified book to the library.

        :param book_object: a Book
        :precondition: book_object must be of the type Book
        :postcondition: correctly adds the specified book to the library, if the argument passed to it is not of a
        book, it will raise a TypeError

        >>> library_one = Library()
        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one.add_books(book_one)
        >>> library_one
        Library([Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)])
        """
        if type(book_object) is not Book:
            raise TypeError("You can only add books to the library")
        else:
            self.libraries.append(book_object)

    def update_library(self, original, new_shelf):
        """Update the specified original book object's shelf attribute with the specified new_shelf.

        :param original: a book
        :param new_shelf: a string or a positive number
        :precondition original: a book object
        :precondition new_shelf: a string or a positive number indicating the new location of the book
        :postcondition: correctly updates the library by updating the shelf attribute of the indicated book

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.update_library(book_one, 2)
        >>> library_one
        Library([Book(Mahan, Tears in the time of Corona, Independent, 2, Life, Slice of Life)])
        """
        book_index = self.libraries.index(original)
        updated_book = original.change_shelf(new_shelf)
        self.libraries[book_index] = updated_book

    def search_library_by_author(self, author):
        """Find books by author.

        :param author: a string
        :precondition: author must be a string
        :postcondition: correctly finds all the books whose author attribute  match (fully or partially) the provided
        argument
        :return: a list of the books whose authors match the given argument

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_author("Mahan")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_author("Ma")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        """
        search_result = []
        for books in self.libraries:
            if author.casefold().strip() in books.author.casefold():
                search_result.append(books)
        return search_result

    def search_library_by_title(self, title):
        """Find books by title.

        :param title: a string
        :precondition: title must be a string
        :postcondition: correctly finds all the books whose title attribute  match (fully or partially) the provided
        argument
        :return: a list of the books whose title match the given argument

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_title("Tears in the time of Corona")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_title("time")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        """
        search_result = []
        for books in self.libraries:
            if title.casefold().strip() in books.title.casefold():
                search_result.append(books)
        return search_result

    def search_library_by_publisher(self, publisher):
        """Find books by publisher.

        :param publisher: a string
        :precondition: publisher must be a string
        :postcondition: correctly finds all the books whose publisher attribute  match (fully or partially) the provided
        argument
        :return: a list of the books whose publisher match the given argument

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_publisher("Independent")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_publisher("de")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        """
        search_result = []
        for books in self.libraries:
            if publisher.casefold().strip() in str(books.publisher).casefold():
                search_result.append(books)
        return search_result

    def search_library_by_shelf(self, shelf):
        """Find books by shelf.

        :param shelf: a string
        :precondition: shelf must be a string
        :postcondition: correctly finds all the books whose shelf attribute  match the provided
        argument
        :return: a list of the books whose shelf match the given argument

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_shelf("1")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        """
        search_result = []
        for books in self.libraries:
            if shelf.casefold().strip() == books.shelf.casefold():
                search_result.append(books)
        return search_result

    def search_library_by_category(self, category):
        """Find books by category.

        :param category: a string
        :precondition: category must be a string
        :postcondition: correctly finds all the books whose category attribute  match (fully or partially) the provided
        argument
        :return: a list of the books whose category match the given argument

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_category("Life")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_category("ife")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        """
        search_result = []
        for books in self.libraries:
            if category.casefold().strip() in books.category.casefold():
                search_result.append(books)
        return search_result

    def search_library_by_subject(self, subject):
        """Find books by subject.

        :param subject: a string
        :precondition: subject must be a string
        :postcondition: correctly finds all the books whose subject attribute  match (fully or partially) the provided
        argument
        :return: a list of the books whose subject match the given argument

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_subject("Slice of Life")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one.search_library_by_subject("Slice")
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)]
        """
        search_result = []
        for books in self.libraries:
            if subject.casefold().strip() in books.subject.casefold():
                search_result.append(books)
        return search_result

    def __str__(self):
        """Provide the information of the Library object.

        :return: the Library object's information

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> print(library_one)
        [Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)] contains 1 books.
        """
        return f"{self.libraries} contains {len(self.libraries)} books."

    def __repr__(self):
        """Provide the attributes of the Library object.

        :return: the attributes of the Library object

        >>> book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        >>> library_one = Library()
        >>> library_one.add_books(book_one)
        >>> library_one
        Library([Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)])
        """
        return f"Library({self.libraries})"


def menu():
    """Ask user for their input.

    :return: a valid input from the user
    """
    input_list = [(index, option) for index, option in
                  enumerate(["Search for a book", "Move a book to a new shelf", "Exit the program"], 1)]
    user_choice = input(f"Please type a number to choose the corresponding option {input_list}")
    while user_choice not in ["1", "2", "3"]:
        user_choice = input(f"That is not a valid option, please try again. {input_list}")
    return user_choice


# def is_number(shelf):
#     try:
#         float(shelf)
#         return True
#     except ValueError:
#         return False


def process_chosen_user_command(user_choice, library):
    """Pass the user's command to the appropriate function.

    :param user_choice: a string
    :param library: a library
    :precondition user_choice: a string ("1" or "2") corresponding to the user's command to either search for a book
    in the library or to update the shelf of a book, respectively
    :precondition library: a library that contains book objects that the user can search for and change the shelves
    :postcondition: if the user chooses "1" (i.e., search for a book), a list of the books that meet the specified
    parameters will be printed, otherwise, the shelf attribute of the chosen book is updated in the library
    :return: the library with update shelf number for the chosen book (only if the user chooses to update the shelf,
    otherwise, there is no return and only the result of their search is printed)
    """
    if user_choice == "1":  # "1" means user wants to search for a book
        search_parameter = search_criteria()  # asking how he wants to search (e.g., author/title/...
        search_result = perform_book_search(search_parameter, library)
        print_search_result(search_result)
    elif user_choice == "2":
        library = update_shelf(library)
        return library


def search_criteria():
    """Prompt user to choose their desired search criterion.

    :return: a valid search criterion
    """
    input_list = [(index, option) for index, option in
                  enumerate(["Search by author", "Search by title", "Search by publisher", "Search by shelf",
                             "Search by category", "Search by subject"], 1)]
    search_parameter = input(f"Please type a number to choose the corresponding option {input_list}")
    while search_parameter not in ["1", "2", "3", "4", "5", "6"]:
        search_parameter = input(f"That is not a valid option, please try again. {input_list}")
    return search_parameter


def perform_book_search(search_parameter, library):
    """Search for book that the user is looking for based on their chosen parameter.

    :param search_parameter: a string
    :param library: a library
    :precondition search_parameter: a string from the list ["1", "2", "3", "4", "5", "6"] indicating the user's desired
    search criterion
    :postcondition: searches the library for the book that the user is looking for based on the specified criterion
    :return: a list of the books that match the user's chosen search_parameter
    """
    if search_parameter == "1":
        return library.search_library_by_author(input("Who is the author of the book?"))
    elif search_parameter == "2":
        return library.search_library_by_title(input("What is the title of the book?"))
    elif search_parameter == "3":
        return library.search_library_by_publisher(input("Who is the publisher of the book?"))
    elif search_parameter == "4":
        return library.search_library_by_shelf(input("Which shelf are looking for?"))
    elif search_parameter == "5":
        return library.search_library_by_category(input("What category of book are you looking for?"))
    elif search_parameter == "6":
        return library.search_library_by_subject(input("What is the subject of the book?"))


def update_shelf(library):
    """Update the shelf attribute of the user's chosen book in the library.

    :param library: a library
    :precondition: library must be a library
    :postcondition: correctly updates the shelf attribute of the user's chosen book in the library
    :return: the updated library
    """
    print("To move a book to another shelf, please first look it up:")
    search_parameter = search_criteria()
    search_result = perform_book_search(search_parameter, library)
    print_search_result(search_result)
    if len(search_result) > 0:
        book_to_be_moved = int(input("Please type in the number corresponding to the book you wish to have moved:"))
        while book_to_be_moved > len(search_result) or book_to_be_moved < 1:
            book_to_be_moved = int(input("That number does not exist in your search result, pleas try again:"))
        book_index = search_result[book_to_be_moved - 1]
        shelf_to_be_moved_to = input("Please type in the new shelf number:")
        library.update_library(book_index, shelf_to_be_moved_to)
        return library


def check_if_json_exists():
    """Convert the "somebooks.json" file to a list if it exists in the directory, otherwise convert the excel file in
    the directory to a list.

    :return: a list of books
    """
    if path.exists("somebooks.json"):
        book_list = open_json_file()
        return book_list
    else:
        book_list = convert_excel_to_list()
        formatted_book_list = remove_decimal_from_shelf_values(book_list)
        return formatted_book_list


def remove_decimal_from_shelf_values(book_list):
    """Remove the decimal from the shelf elements of the book_list that end with ".0".

    :param book_list: a list
    :precondition: book_list must be a list of books
    :precondition: removes the ".0" from the shelf values that have it
    :return: updated book_list where no shelf value is in decimal format

    >>> test_book_list = [{'author': 'Mahan', 'shelf': '2.0'}]
    >>> remove_decimal_from_shelf_values(test_book_list)
    [{'author': 'Mahan', 'shelf': '2'}]
    """
    for item in book_list:
        if item['shelf'].endswith('.0'):
            item['shelf'] = item['shelf'].removesuffix('.0')
    return book_list


# def convert_empty_cells_to_none(book_list):
#     for item in book_list:
#         if item['publisher'] == "":
#             item['publisher'] = None
#     return book_list


def open_json_file():
    """Open "somebooks.json" file and load it's contests as a list.

    :return: a list of the data in the "somebooks.json"
    """
    file_name = "somebooks.json"
    with open(file_name, 'r') as json_file:
        book_list = json.load(json_file)
    return book_list


def convert_excel_to_list():
    """Convert the excel file to a list.

    :return: a list of dictionaries containing the key-value pairs for each book
    """
    workbook = xlrd.open_workbook(
        r"somebooks.xls")  # (r"C:/Users/mahan/PycharmProjects/a5-book-manager-MahanZadeh/somebooks.xls")
    sheet = workbook.sheet_by_name("Books")
    book_list = []
    for row in range(1, sheet.nrows):
        books = {}
        row_values = sheet.row_values(row)
        books['author'] = row_values[0]
        books['title'] = row_values[1]
        if row_values[2] == "":
            books['publisher'] = None
        else:
            books['publisher'] = row_values[2]
        books['shelf'] = str(row_values[3])
        books['category'] = row_values[4]
        books['subject'] = row_values[5]
        book_list.append(books)
    return book_list


def create_library_of_book_objects(book_list):
    """Create a library of book objects from the given book_list.

    :param book_list: a list
    :precondition: a list of dictionaries containing keys [author, publisher, shelf, category, subject] and their
    corresponding values
    :postcondition: converts the given list the a library of book objects
    :return: a library filled with book objects

    >>> test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',\
     'subject': 'Life'}, {'author': 'Chris', 'title': 'Smiles', 'publisher': 'Self', 'shelf': '2', 'category': 'Life',\
     'subject': 'Life'}]
    >>> create_library_of_book_objects(test_book_list)
    Library([Book(Mahan, Tears, Self, 1, Life, Life), Book(Chris, Smiles, Self, 2, Life, Life)])
    """
    new_library = Library()
    for item in book_list:
        book_object = Book(item['author'], item['title'], item['publisher'], item['shelf'], item['category'],
                           item['subject'])
        new_library.add_books(book_object)
    return new_library


def print_search_result(list_of_books):
    """Print the result of the search.

    :param list_of_books: a list
    :precondition: list_of_books must be a list containing only Book objects
    :postcondition: correctly prints the number of results and the details of each book item
    """
    print(f"There are {len(list_of_books)} books that match your search criteria:\n")
    counter = 1
    for item in list_of_books:
        print(f"({counter})-- {item}")
        counter += 1


def convert_library_to_json(library):
    """Convert library of books to a JSON file.

    :param library: a library
    :precondition: a library containing book objects
    :postcondition: converts each book in the library to a dictionary containing keys [author, publisher, shelf,
    category, subject] and their corresponding values
    :return: a JSON file containing the data of the books in the library
    """
    file_name = "somebooks.json"
    dict_file = []
    with open(file_name, 'w') as file_object:
        for book in library:
            dictionary = {'author': book.author, 'title': book.title, 'publisher': book.publisher, 'shelf': book.shelf,
                          'category': book.category, 'subject': book.subject}
            dict_file.append(dictionary)
        json.dump(dict_file, file_object, indent=2)
    return file_object


def main():
    """Drive the program"""
    book_list = check_if_json_exists()
    library = create_library_of_book_objects(book_list)
    exist_program = False
    while exist_program is False:
        user_choice = menu()
        if user_choice != "3":
            process_chosen_user_command(user_choice, library)
        else:
            convert_library_to_json(library.libraries)
            exist_program = True
    print("Thank you for visiting Chris's library, please come again!")


if __name__ == "__main__":
    main()
