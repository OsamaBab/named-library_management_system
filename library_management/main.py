
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

    # Welcome message to the Library user
    print("\nWelcome to the Bradford College Library Management System!\n")

    # Loop to display menu with handlling the user selections
    while True:
        # Display menu options to the user from 1 to 9
        print("\nSelect An Option Please:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Add a member")
        print("4. Remove a member")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. List available books")
        print("8. List borrowed books")
        print("9. Exit")
        
        # Get the user's selection and loop with handlling any invalid input 
        try:
            selection = int(input("\nEnter your selection: ")) # input numbers 
        except ValueError:
            # Display this message handlling any invalid input 
            print("Invalid input! Please enter a number between 1 and 9.")
            # Loop the selection input 
            continue

        # if Option 1 is selected = Add a new book to the library
        if selection == 1:
            title = input("Enter book title: ").strip()  # input the book's title and get it
            author = input("Enter book author: ").strip()  # input the book's author name and get it
            # call function to add the book to the library
            library.add_book(Book(title, author))
            # Display confirmation message of added book datils
            print(f"Book '{title}' by {author} added to the library.") 

        # if Option 2 is selected = Remove a book from the library
        elif selection == 2:
            title = input("Enter the title of the book to remove: ").strip()  # Enter and get the title of the book to remove
            book_to_remove = next((book for book in library.books if book.title.lower() == title.lower()), None)
            # Check this book exsistentce in the library collection
            if book_to_remove:
                library.remove_book(book_to_remove)  # Remove the book if it is exsist
                # Display confirmation message of the removed book title
                print(f"Book '{title}' removed from the library.")

            else:
                print(f"No book titled '{title}' found in the library.") 

        # if Option 3 is selected = Add a member to the library
        elif selection == 3:
            member_type = input("Is the member a student or a teacher? (student/teacher): ").strip().lower()
            name = input("Enter member name: ").strip()  # Get the member's name

            # Create a StudentMember or TeacherMember based on user input
            if member_type == "student":
                student_id = input("Enter student ID: ").strip()
                member = StudentMember(name, student_id)
            elif member_type == "teacher":
                teacher_id = input("Enter teacher ID: ").strip()
                member = TeacherMember(name, teacher_id)
            else:
                print("Invalid member type. Please choose either 'student' or 'teacher'.")
                continue

            library.add_member(member)  # Add the member to the library
            members_map[name] = member  # Map the member's name to their object
            print(f"Member '{name}' added to the library.")

        # if Option 4 is selected = Remove a member from the library
        elif selection == 4:
            name = input("Enter the name of the member to remove: ").strip()  # Get the member's name
            member = members_map.get(name)
            if member:
                library.remove_member(member)  # Remove the member
                members_map.pop(name)  # Remove the member from the map
                print(f"Member '{name}' removed from the library.")
            else:
                print(f"No member named '{name}' found.")

        # if Option 5 is selected = Borrow a book
        elif selection == 5:
            name = input("Enter the member's name: ").strip()  # Get the member's name
            member = members_map.get(name)
            if not member:
                print(f"No member named '{name}' found.")
                continue

            title = input("Enter the title of the book to borrow: ").strip()  # Get the book title
            book_to_borrow = next((book for book in library.books if book.title.lower() == title.lower()), None)
            if book_to_borrow:
                library.borrow_book(book_to_borrow, member)  # Allow the member to borrow the book
                print(f"Book '{title}' borrowed by {name}.")
            else:
                print(f"No book titled '{title}' available in the library.")

        # if Option 6 is selected = Return a book
        elif selection == 6:
            name = input("Enter the member's name: ").strip()  # Get the member's name
            member = members_map.get(name)
            if not member:
                print(f"No member named '{name}' found.")
                continue

            title = input("Enter the title of the book to return: ").strip()  # Get the book title
            book_to_return = next((book for book in member.borrowed_books if book.title.lower() == title.lower()), None)
            if book_to_return:
                library.return_book(book_to_return, member)  # Allow the member to return the book
                print(f"Book '{title}' returned by {name}.")
            else:
                print(f"No book titled '{title}' found in {name}'s borrowed books.")

        # if Option 7 is selected = List all available books
        elif selection == 7:
            print("\nAvailable Books:")
            library.list_available_books()  # Display all available books in the library

        # if Option 8 is selected = List all borrowed books
        elif selection == 8:
            print("\nBorrowed Books:")
            library.list_borrowed_books()  # Display all borrowed books and their borrowers

        # if Option 9 is selected = Exit the program
        elif selection == 9:
            # Check for termination condition
            user_input = input("Do you want to exit realy? (y/n): ")
            try:
                if user_input.lower() == "y":
                    print("\nThank you . See You Soon!")
            except Exception as e:
                print(f"An error occurred: {e}")
            # Exit the loop and end the program if y is input
            break  

        # Display a message and handle invalid selection
        else:
            print("Invalid selection! Please enter a number between 1 and 9.")

# The main entry point for the Library System
if __name__ == "__main__":
    main()
