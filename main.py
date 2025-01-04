
# Importing required classes
from Classes.library import Library
from Classes.book import Book
from Classes.member import Member, StudentMember, TeacherMember

def main():
    """
        Description:
        The main function and entry point to the Library Management System for users to manage library operations.
      
    """

    # creating and initialising the library instance to using it
    library = Library()
    # Create A dictionary to sort and store member names to their respective Member objects for easer and quick access
    membership_map = {}
    
    # Welcome message to the Library user
    print("\nWelcome to the Bradford College Library Management System!\n")

    # Loop to display menu with handlling the user selections
    while True:
        # Display menu options to users from 1 to 9
        print("\nChoose An Option From (1-9)Please: ")
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
            # input the choice numbers 
            choice = int(input("\nEnter your selection: ")) 
        except ValueError:
            # Display this message handlling any invalid input 
            print("Sorry! Invalid input, Please enter a number between 1 and 9.")
            # Loop the selection input 
            continue
        # Choose this choice to add new books to the library book list
        if choice == 1:
            # input the book's title and get it
            title = input("Input The New Book Title: ").strip() 
            # input the book's author name and get it
            author = input("Input New Book Author's Name: ").strip()  
            # Create a new book object and call function to add the book to the library
            library.add_book(Book(title, author))
             
        # Choose this choice to remove a book from the library books list
        elif choice == 2:
            # Enter and get the title of the book to be removed ignoring the entered characters case
            title = input("Input The Book's Title To Remove: ").strip()  
            # Use next function to match the input title with books titles in the library books list or return none
            book_to_be_removed = next((book for book in library.books if book.title.lower() == title.lower()), None)
            # Check this book exsistentce in the library collection
            if book_to_be_removed:
                # Call the function to remove the book from the library books list
                library.remove_book(book_to_be_removed)              
            else:
                # Display a messege with the book tiltle if not found
                print(f"Sorry! This Book  '{title}' is not exsist in the library collection.")
 
        # Choose this choice to add a member to the library membership list
        elif choice == 3:
            membership_type = input("Input (student) or (teacher) for membership type please!: ").strip().lower()
            # Get the member's name
            name = input("Input the member's name: ").strip()  
            # Check this name exsistance in the membership mapbefore adding it to prevent the dublication
            if name in membership_map:
                # Display this exsistance message 
                print(f"Member '{name}' already exists in the library.")
                # Continue in the process if the name dose not exsist
                continue
            # Create a StudentMember or TeacherMember based on user input
            if membership_type == "student":
                # Get Student id
                student_id = input("Input the student ID: ").strip()
                member = StudentMember(name, student_id)
            elif membership_type == "teacher":
                teacher_id = input("Input the teacher ID: ").strip()
                member = TeacherMember(name, teacher_id)
            else:
                # Display this message to inform the invalied input
                print("Sorry! Invalid member type. Input either 'student' or 'teacher' please.")
                # continue the adding member process
                continue
            # call the fuction to add the member to the library collection
            library.add_member(member)  
            # Sort out the membership by adding the members to membership map based on their object type 
            membership_map[name] = member 
            # display this message
            print(f"The {membership_type} {name} is successfully added to the library membership.")

        # Choose this choice to remove members from the library membership
        elif choice == 4:
            # Get the name of the member
            name = input("Enter the name of the member to remove: ").strip()  
            # Get this name from the member map list if is exsist
            member = membership_map.get(name)
            # Check if this name is in the library membership
            if member:
                # Remove this member from the library membership
                library.remove_member(member) 
                # Remove this member from the member map 
                membership_map.pop(name)  
                # Display the removed memeber details
                print(f"The {membership_type} '{name}' removed from the library.")
            else:
                # Display this message if this name is not a member
                print(f"Sorry! This '{name}' name is NOT a member. Please register first.")

        # Choose this choice to borrow books from the library books list
        elif choice == 5:
            # Get the name of the member
            name = input("Input the member's name: ").strip()  
            # Get this name from the member map list if is exsist
            member = membership_map.get(name)
            # Check if this name is in the library membership
            if not member:
                # Display this message if this name is not a member
                print(f"Sorry! This '{name}' name is NOT a member. Please register first.")
                # Continue the return process is the name is a member
                continue
            # Get the title of the book 
            title = input("Please input the title of the book tilte to borrow: ").strip()  
            # Check the book availability in the library books list 
            book_to_borrow = next((book for book in library.books if book.title.lower() == title.lower()), None)
            if book_to_borrow:
                # Call the function to allow the member borrow the book
                library.borrow_book(book_to_borrow, member)  
                # Display this message with the book title and who borrowed this book
                print(f"The Book '{title}' is borrowed by {name} now.")
            else:
                # Display this message with the unavailable book title
                print(f"Sorry! The '{title}' book is NOT available in the library at the moment.")

        # Choose this choice to return books to the library books list
        elif choice == 6:
            # Get the name of the member
            name = input("Input the member's name please: ").strip()  
             # Get the member's name from the membership map list
            member = membership_map.get(name)
            # Check if this name is in the library membership list
            if not member:
                # Display this message if this name is not a member
                print(f"Sorry! This '{name}' name is not a member. Please register first.")
                # Continue the return process is the name is a member
                continue
            title = input("Please input the book title to return: ").strip()  # Get the book title
            # Check the returned book availability in the borrowed books list
            book_to_return = next((book for book in member.borrowed_books if book.title.lower() == title.lower()), None)
            if book_to_return:
                library.return_book(book_to_return, member)  # Allow the member to return the book
                # Display this message with the book title and who returned this book
                print(f"Thank you {name}. The Book '{title}' is returned now.")
            else:
                 # Display this message with the unavailable book title
                print(f"Sorry! The '{title}' book is NOT available in the library at the moment.")
                
        # Choose this choice to list all available books in the library collection
        elif choice == 7:
            # Display this title
            print("\nThe Available Books List:")
            # Call the function to list all aiavlable books in the library
            library.list_available_books()  
            
        # Choose this choice to list all borrowed books
        elif choice == 8:
            # Display this title
            print("\nThe Borrowed Books List:")
            # call the function to list all borrowed books and their borrowers
            library.list_borrowed_books()  

        # Choose this choice to Exit the program
        elif choice == 9:
            # Check for termination condition
            user_input = input("Do you want to exit realy? (y/n): ")
            # Error hanlling 
            try:
                if user_input.lower() == "y":
                    print("\nThank you . See You Soon!")
            except Exception as e:
                print(f"An error occurred: {e}")
            # Exit the loop and end the program if y is input
            break  
        else:
            # Display a message and handle invalid selection
            print("Invalid selection! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    # Run the main entry point for the Library System
    main()
