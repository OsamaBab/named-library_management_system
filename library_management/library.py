class Library:
    """
    Represents a library.
    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    """
    def __init__(self):
        """
        Constructs an empty library.
        Attributes:
        - books (list): A list to store books in the library collection.
        - members (list): A list store members in the library.
        """
        self.books = []
        self.members = []

    def add_book(self, book):
        """
        Adds a book to the library collection list

        Args:
        - book (Book): The book to be added.
        """
        # Update the books list after inputing the new book details
        self.books.append(book) 
        # Display a successful messege with the added book details
        print(f"Book: {book} is added successfully to the library collection")

    def remove_book(self, book):
        """
        Removes a book from the library.

        Args:
        - book (Book): The book to be removed.
        """
        # If statment to check the book exsistence
        if book in self.books:
            # Remove the selected book from the library list collection  
            self.books.remove(book)
            # Display a successful messege with the removed book tiltle
            print(f"Book: '{book.title}' is removed successully from the library collection.") 
        else:
            # Display a messege with the book tiltle if not found
            print(f"Book '{book.title}' not exsist in the library collection.")

    def add_member(self, member):
        """
        Adds a member to the library.

        Args:
        - member (Member): The member to be added.
        """
        # Add the new member to the library collection list
        self.members.append(member)

    def remove_member(self, member):
        """
        Removes a member from the library.

        Args:
        - member (Member): The member to be removed.
        """
        # If statment to check the member exsistence
        if member in self.members:
            # Remove the selected member from the library list collection
            self.members.remove(member)
            # Display a successful messege with the removed member name
            print(f"This: '{member.name}' is removed successully from the library collection.") 
        else:
            # Display a messege with the member name if not found
            print(f"Member '{member.name}' not found in the library.") 
        
    def borrow_book(self, book, member):
        """
        Allows a member to borrow a book from the library.

        Args:
        - book (Book): The book to be borrowed.
        - member (Member): The member borrowing the book.
        """
        # If statment to check the book exsistence in the library and borrowed book lists
        if book in self.books:
            self.books.remove(book) # Remove book from available books
            book.available = False  # Mark book as unavailable in the library
            member.borrow_book(book) # Add book details to the member's borrowed list ollection
        else:
            # Display a messege with the book title if not available to borrow
            print(f"This Book: '{book.title}' is not available to borrow.")

    def return_book(self, book, member):
        """
        Allows a member to return a book to the library.

        Args:
        - book (Book): The book to be returned.
        - member (Member): The member returning the book.
        """
        self.books.append(book)
        member.return_book(book)

    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")

    def list_borrowed_books(self):
        """
        Lists all borrowed books and their borrowers.
        """
        for member in self.members:
            for book in member.borrowed_books:
                print(f"Title: {book.title}, Author: {book.author}, Borrower: {member.name}")