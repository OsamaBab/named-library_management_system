
class Library:
    """
    Description:
    A class to represents a library books list, member list and the library information.
    """
    def __init__(self,library_name=None, contact=None, address=None):
        """
        Description:
        Constructs the library class and initialise its attributes.
            Attributes:
            library name (str): The librarry name
            contact (str): The library contact information
            address (str): The library address
            books (list): A list to store books in the library collection.
            members (list): A list to store members in the library collection.
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
        # Update the books list after adding a new book details
        self.books.append(book) 
        # Display confirmation message of the new added book datils
        print(f"The New Added Book Details:\nBook Title: {book.title} Author Name: {book.author}")
       
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
            # Display confirmation message of the removed book title
            print(f"The Removed Book Details:\nBook Title: {book.title} Author Name: {book.author}")
       
    def add_member(self, member):
        """
        Description:
        Adds a member to the library.
            Args:
            - member (Member): The member to be added.
        """
        # Check the memeber exsistance to prevent dublicating memebership 
        if member in self.members:
            # Display this exsistance message
            print(f"Sorry! this '{member.name}' name is already exists in the library membership.")
        else:
        # Add the new member to the library membership list
            self.members.append(member)

    def remove_member(self, member):
        """
        Description:
        Removes a member from the library.
            Args:
            - member (Member): The member to be removed.
        """
        # Check the member exsistence in the membership list
        if member in self.members:
            # Remove the selected member from the library membership list
            self.members.remove(member)
        else:
            # Display a messege with the member name 
            print(f"Sorry! This '{member.name}' is not found in the library membership list.") 
        
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
            # Remove book from available books
            self.books.remove(book) 
            # Mark this book as unavailable in the library
            book.available = False 
            # Call function to add this book details to the member's borrowed book's list  
            member.borrow_book(book) 
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
            # Call function to remove this book from the member's borrowed book's list
            member.return_book(book)  
            # Mark this book back as available in the library list
            book.available = True
            # Add back the book to the library collection  
            self.books.append(book)  
        else:
            # Display the confirmation returned book message 
            print(f"Book '{book.title}' is not in {member.name}'s borrowed list.")

    def list_available_books(self):
        """
        Description:
        Function to lists all available books in the library collection.
         Return:
            THis function returns available books in a list
        """
        # Check the library collection if found display them with details
        available_books = [book for book in self.books if book.available]
        # Perform available books listing
        if available_books:
            for book in available_books:
                # Display available books listing book title and author name
                print(f"Title: {book.title} |  Author:  {book.author}")
        else:
            # Display this message if no book found
            print("Sorry no any books available in the library.")
       
    def list_borrowed_books(self):
        """
        Description:
        Function to lists all borrowed books and their borrowers from the library collection.
         Return:
            This function return the borrowed books with their borrower name in a list
        """    
        # Assume there is no any book is borrowed by defaul
        borrowed_books = []
        # Find out all members in the library membership list
        for member in self.members:
            # Find out all members that borrowed books from the library books collection
            for book in member.borrowed_books:
                borrowed_books.append((book, member))
                if borrowed_books:   
                    # Display all borrowed books details and the name of the borrower
                    borrowed_books, print(f"The Borrowed Book Title: {book.title}   |  Author: {book.author}  |  Borrower name: {member.name}")       
                else:
                    # Display the message below if no books borrowed
                    print("Sorry! There is No any book is borrowed at the moment.")