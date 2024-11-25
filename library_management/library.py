class Library:
    """
    Description:
    A class to represents a library.
        Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self,library_name, contact, address):
        """
        Description:
        Constructs the library class and initialise its attributes.
            Attributes:
            -library name (str): The librarry name
            -contact (str): The library contact information
            -address (str): The library address
            - books (list): A list to store books in the library collection.
            - members (list): A list to store members in the library collection.
        """
        self.library_name = library_name
        self.contact  = contact
        self.address  = address
        self.books    = []
        self.members  = []

    def add_book(self, book):
        """
        Description:
        Adds a book to the library collection list
            Attributes:
        -   -book (Book): The book to be added.
        """
        # Update the books list after inputing the new book details
        self.books.append(book) 
        # Display a successful messege with the added book details
        print(f"Book: {book} is added successfully to the library collection")

    def remove_book(self, book):
        """
        Description:
        Removes a book from the library.

            Attributes:
            - book (Book): The book to be removed.
        """
        # If statment to check the book exsistence
        if book in self.books:
            # Remove the selected book from the library book list collection  
            self.books.remove(book)
            # Display a successful messege with the removed book tiltle
            print(f"Book: '{book.title}' is removed successully from the library collection.") 
        else:
            # Display a messege with the book tiltle if not found
            print(f"Book '{book.title}' not exsist in the library collection.")

    def add_member(self, member):
        """
        Description:
        Adds a member to the library.
            Args:
            - member (Member): The member to be added.
        """
        # Add the new member to the library collection list
        self.members.append(member)

    def remove_member(self, member):
        """
        Description:
        Removes a member from the library.
            Args:
            - member (Member): The member to be removed.
        """
        # If statment to check the member exsistence in the members list
        if member in self.members:
            # Remove the selected member from the library list collection
            self.members.remove(member)
            # Display a successful removal messege with the removed member name
            print(f"This: '{member.name}' is removed successully from the library collection.") 
        else:
            # Display a messege with the member name if not found
            print(f"Member '{member.name}' not found in the library.") 
        
    def borrow_book(self, book, member):
        """
        Description:
        Allows a member to borrow a book from the library.
            Args:
            - book (Book): The book to be borrowed.
            - member (Member): The member borrowing the book.
        """
        # Check the book exsistence in the library andit is mark is available
        if book in self.books and book.available:
            self.books.remove(book) # Remove book from available books
            book.available = False  # Mark this book as unavailable in the library
            member.borrow_book(book) # Add this book details to the member's borrowed list collection
        else:
            # Display a messege with the book title if not available to borrow
            print(f"This Book: '{book.title}' is not available to borrow.")

    def return_book(self, book, member):
        """
        Description:
        Allows a member to return a book to the library.
            Attributes:
            - book (Book): The book to be returned to the library collection.
            - member (Member): The member returning the book to the library collection..
        """
        # Check if the book is in the member borrowed list
        if book in member.borrowed_books:
            member.return_book(book)  # Remove this book from the member's borrowed list
            book.available = True  # Mark this book back as available
            self.books.append(book)  # Add back the book to the library collection
        else:
            # Display the confirmation returned book message 
            print(f"Book '{book.title}' is not in {member.name}'s borrowed list.")

    def list_available_books(self):
        """
        Description:
        Function to lists all available books in the library collection.
        """
        # Check the library collection if found display them with details
        if self.books:
            for book in self.books:
                if book.available:
                    print(f"Title: {book.title}, Author: {book.author}")
        else:
            # Display this message if no book found
            print("Sorry no any books available in the library.")

    def list_borrowed_books(self):
        """
        Description:
        Function to lists all borrowed books and their borrowers from the library collection.
        """
        borrowed_books_isfounded = False
        # Find out all members that borrowed books from the library collection
        for member in self.members:
            for book in member.borrowed_books:
                borrowed_books_isfounded = True
                # Display all borrowed books details and the name of the borrower
                print(f"The Borrowed Book Title: {book.title}, Author: {book.author}, Borrower name: {member.name}")
        # Display the message below if no books borrowed
        if not borrowed_books_isfounded:
            print("No borrowed books currently.")