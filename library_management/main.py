
# Importing required classes
from library import Library
from book import Book
from member import Member, StudentMember, TeacherMember

def main():
    """
        Description:
        The main function and entry point to the Library Management System for users to manage library operations.
      
    """


    # Initialising the library instance 
    library = Library()

    # Create A dictionary to sort member names to their respective Member objects for quick access
    members_map = {}

    # Welcome message to the user
    print("\nWelcome to the Bradford College Library Management System!\n")

    # Loop to display menu with handlling the user selections
    while True:
        # Display menu options to the user
        print("\nSelect An Option Please:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Add a member")
        print("4. Remove a member")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. List all available books")
        print("8. List all borrowed books")
        print("9. Exit")
        
        # Get the user's selection with handlling any invalid input 
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            # Display this message 
            print("Invalid input! Please enter a number between 1 and 9.")
            continue


if __name__ == "__main__":
    main()
