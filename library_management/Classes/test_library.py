# Import all required files
import unittest
from book import Book
from library import Library
from member import  Member, TeacherMember, StudentMember

def create_instance():
    """
    Description: 
    Function to create instances for all classes  and retun their values for testing purpose.
        Attributes:
        -class (object): The object of a class to create a new object form it
    """
    # Print this title 
    print("Creating The Library Systm's Instances ")
    # Create a new instance of the Book class
    try:
        # Print this title 
        print("## Created The Library Systm's Instances Lis##")
        # Create new books instances from the Book class
        book1 = Book("Advance programming", "Newten Clark")
        book2 = Book("Under the Sun", "Joker G.Smith")
        # Display a message with the new created books objects' details
        print("Books have been created successfully:.\nBook1: ", book1, "\nBook2: ", book2)
    except NameError as e:
        # Handle the error with the error name and display an error message if the new book object creation is failed 
        print("The Error Of Creating The Book Instance Is: ", e)
    try:
        # Create a new instance of the Library class
        library = Library()
        # Display a message with the new created library object's details
        print("Library instance has been created successfully:", library)
    except NameError as e:
        # Handle the error with the error name and display an error message if the new library's object creation is failed 
        print("The Error Of Creating The Library Instance List: ", e)
    # Create a new instance of the student Member and teacher Member classes
    try:
        # Create a new student object and pass the student name with id to this new object
        student = StudentMember("Mr. Osama", "S10593")
        # Create a new teacher object and pass the teacher name with id to this new object
        teacher = TeacherMember("Mr. Gen", "T25858")
        # Test the created new books with displaying a message and books details
        print("Members has been created successfully:\nStudent Detils: ", student,"\nTeacher Detils: ", teacher)
    # Handle the error with the error name and display an error message if the new stuent and teacher objects creation is failed 
    except NameError as e:
        print("There is an error Of Creating The Member Instance Is: ", e)
    # Retun the all created instaces values 
    return book1, book2, library, student, teacher


# Testing The Library System Operations 
class TestLibrarySstem(unittest.TestCase):
    """
    This Class tests the library key operations using the unittess TestCases

    """
    def setUp(self):
        """
        This method is Setting up and initialising fresh instancees of Library system classes for each test.
        """
        # Initialise a library instace
        self.library = Library()
        # Create two book's instances and name them Book1 and Book2
        self.book1 = Book("Python For ML", "Kair Mano")
        self.book2 = Book("Coding Python", "Hanim Grage")
        # Add crated Book1 to the library books list
        self.library.add_book(self.book1)
        # Add crated Book2 to the library books list
        self.library.add_book(self.book2)

    def test_add_book(self):
        """
        This method tests add book function to add a new book to the library books list.
        """
        # Create a new book
        book3 = Book("Problem Solving", "Samri Huang")
        # Add the created new book to the library book's list
        self.library.add_book(book3)
        # Test ans assert if the added new book is exsisted in the library books list
        self.assertIn(book3, self.library.books)

    def test_remove_book(self):
        """
        This function tests remove book function to remove and exsisted book from the library books list.
        """
        # Call the function to emove created Book1 from the library books list
        self.library.remove_book(self.book1)
        # Test and assert if the Book1 is exsisted in the library books list
        self.assertNotIn(self.book1, self.library.books)
        
    def test_add_member(self):
        """
        This function tests add member function to add new members to the library membership list.
        """
        # Create a new member
        self.member1 = Member("Hull")
        # Perform the add member function to add the created new member to the liprary membership list
        self.library.add_member(self.member1)
        # Test and assert if the added member is exsisted in the library membership list
        self.assertIn(self.member1, self.library.members)

    def test_borrow_book(self):
        """
        This function tests borrow book function to borrow available books by members
        """
        # Create a new member
        member = Member("Adam")
        # Perform the add member function to add the created new member to the liprary membership list
        self.library.add_member(member)
        # Perform the borrow book function to borrow Book1 that is already removed from the library books list.
        self.library.borrow_book(self.book2, member)
        # Test and assert if the Book1 is NOT exsisted in the library books list
        self.assertNotIn(self.book2, self.library.books)
        # Test and assert if the Book1 is exsisted in the member's borrowed books's  list
        self.assertIn(self.book2, member.borrowed_books)

    def test_list_available_books(self):
        """
        This function tests list available book function to list available books in the library books list.
        """
        # Asume the library books list is cleared 
        self.library.books = []  
        # Create a new book object
        book = Book("Problem Solving", "Samri Huang")
        # Add the created new book to the library book's list
        self.library.add_book(book)
        # Create a variable to store available books in the library
        available_books = self.library.list_available_books(book)
        # Test and assert if the available books stored in the variable is equal to the books in the books list
        self.assertNotEqual(available_books, [])  
        
    def test_list_borrowed_books(self):
        """
        This function tests list borrowed books function that lists all borrowed books from the the library books list.
        """
         # Asume the library books list is cleared 
        self.library.books = []  
         # Create a new book object
        book = Book("Problem Solving", "Samri Huang")
        # Add the created new book to the library book's list
        self.library.add_book(book)
        # Create a new member
        member = Member("Man")
        # Perform the add member function to add the created new member to the liprary membership list
        self.library.add_member(member)
        # Perform the borrow book function to borrow Book1 that is already removed from the library books list.
        self.library.borrow_book(book, member)
        # Store borrowed books list in a variable
        borrowed_books = self.library.list_borrowed_books()
        # Test and assert if the books list and borrowed bookslist
        self.assertNotEqual(borrowed_books, [])  
if __name__ == '__main__':
    # Run the test
    unittest.main()