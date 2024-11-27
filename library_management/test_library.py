# Import all required files
from book import Book
from library import Library
from member import Member, TeacherMember, StudentMember

"""
Description: 
This file to test library classes and functionss.
Test Classes and Methods here
"""
def create_instance():
    """
    Description: 
    Function to create instances for all classes for testing purpose.
        Attributes:
        -class (object): The object of a class to create a new object form it
    """
    
    # Create a new instance of the Book class
    try:
        # Create a new book object and pass the book title and author to it
        book1 = Book("Advance programming", "Newten Clark")
        book2 = Book("Under the Sun", "Joker Smith")
        # Test the created new books with displaying a message and books details
        print("Books have been created successfully:", book1, book2)
    # Handle the error of the created books instances with a message
    except NameError as e:
        print("Error creating Book instances:", e)
    
    # Create a new instance of the Library class
    try:
        library = Library()
        print("Library instance has been created successfully:", library)
    except NameError as e:
        # Handle the error of the created library instances with a message
        print("Error creating Library instance:", e)

    # Create a new instance of the student Member and teacher Member classes
    try:
        # Create a new student object and pass the student name with id to this new object
        student = StudentMember("Mr. Osama", "S10593")
        # Create a new teacher object and pass the teacher name with id to this new object
        teacher = TeacherMember("Mr. Gen", "T25858")
        # Test the created new books with displaying a message and books details
        print("Members created successfully:", student, teacher)
    # Handle the error of the created books instances with a message
    except NameError as e:
        print("Error creating Member instances:", e)
    # 
    return book1, book2, library, student, teacher

'''
Library Operations
'''
def library_operations():
    """
    Simulating the created instances with library operations.
    """
    print("\nSimulating library operations...")

    # Create initial objects to cover all operations
    book1, book2, library, student, teacher = create_instance()


    # Add created books to the library collection
    ## Call the available books function from library class to
    library.add_book(book1)
    # Call the available books function from library class to
    library.add_book(book2)

    # Add created members to the library
    ## Call add member function from library class and pass student created object to be added to the library
    library.add_member(student)
    # Call add member function from library class and pass teacher created object to be added to the library
    library.add_member(teacher)

    # List available books in the library
    print("\nAvailable books in the library:") # Display this message
    # Call the available books function from library class to list all available books in the library
    library.list_available_books()

    # Borrow a book from the library
    ## Display a string message
    print("\nBorrowed books:")
    # Call the function from library class to list all borroed books from the library
    library.list_borrowed_books()

    # Return a book
    ## Display a string message
    print("\nAlice returns '1984':")
    # Call the function from library class and pass a book title and student name to return this book to the library
    library.return_book(book1, student)
   

# Run the test suite
if __name__ == "__main__":
    library_operations()