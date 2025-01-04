### Library Management System

## Project Overview
This project aims to create a Python application that simulates a simple real-world library management system scenario involving the use of Object-Oriented Programming (OOP) techniques and principles such as classes, inheritance, encapsulation, abstraction and polymorphism  in terms of managing a collection of library members and books via enabling the basic functionalities such as:
- Add books / new members
- Remove books / existent members
- Borrow books
- Return books
- List available books
- List borrowed books.
Documentation is included to ensure clarity as well as Testing for usability and maintainability.
## The objectives:
Facilite the core library system's pre-defined operations.
Organise the library collections such as books and members, and enabl efficient tracking for them.
Ensuring the code scalability,reusability and maintaiability via demonstrating the Object-Oriented Programming core principles implementation.
## The System Features
1.  Book Management Feature:
Add and remove books from the library system.
2. Member Management Feature: 
Add and remove members from the the library system.
3. Borrowing/Returning Books Features: 
Enable the library members to borrow and return books.
4. Books' Availability Checking Feature: 
List all exsistant and borrowed books with borrower's information.
5. Library Users' Types: 
Differentiate between members types as student and teacher.
## System Structure
```
library_management_system/
├── Classes/
│   ├── __init__.py
│   ├── library.py
│   ├── book.py
│   ├── member.py
│   └── test_library.py
|── main.py
├── README.md
└── requirements.txt
```  
## Classes and Methods
# Library Class
The Library class manages books and members collections. It serves as the central hub between The Book and Member classes.
## Methods
- Add Book Method: This function adds a book to the library's books list collection.
Remove Book Method: It removes Avialable books in the library books list.
- Add Member Method: This function enable new users to register a new membership. it is a dublicated-free method.
- Remove Member Method: this function is a reverse add members method. It removes an existing membership from the libary membership list.
- Borrow Book Method: It enable the library members to borrow available books in the library books list.
- Return Book Method: It enable the books brrowers to return their borrowed books in their borrorowed lis to the library books list.
- List Available Books Method: this function lists all books that are currently available in the library books list.
- List Borrowed Books Method: this function lists all books that are currently borrowed by members along with borrowers details.
# Book Class
The Book class represents each book details in the library such as books titles and authors of books.
## Methods
Book class includes string representer method to represent books details as strings for testing and debugging purposes.
# Member Class
The Member class represents a library's memberships with basic details such as name.
Member class includes two subclasses, Member Student class and Member Teacher class. These subclasses serve as special extention to the member class via adding the id attribute that differentiates between students membership and teachers membership helping in the membership management accross the library key operations.
## Methods
The Student and Teacher Member classes include string representer methods to represent these two subclasses attributes for testing and debugging purposes.
## Setup Instructions
1. Download the repository to your local machine using this link:  
 https://github.com/OsamaBab/Console-based-Banking-Application/archive/refs/heads/main.zip  
2. Clone the repository remotely using this command line:   
  git clone https://github.com/OsamaBab/library_management_system.git
3. Direct to the directory of the project: cd library_management_system
4. Install the required dependencies: pip install -r requirements.txt.
5. Run the bank application using command line: python main.py
## The System Usage:
- Add a new book:
  1. Select option 1
  2. Input the book name
  3. Input the author name
  4. Click entre
- Remove a book:
  1. Select option 2
  2. input the book title
  3. Click entre
- Add a new member:
  1. Slect option 3
  2. Input the name
  3. Input a membership type (student/ teacher)
  4. Input user id
  5. Click entre
- Remove a member:
  1. Select option 4
  2. Input a member name
  3. Click entre
- Borrow a book:
  1. Select option 5
  2. Input a member name
  3. Input the book title
  4. Click entre
- Return a book:
  1. Select option 6
  2. Input a member name
  3. Input a book tilte
  4. Click entre
- List available books:
  1. Select option 7
  2. Click entre
- List borrowed books:
  1. Select option 8
  2. Click entre
## Testing
The library system is tested and its fuctionallities are verified and validated via unittest test cases. all the test cases are successfully passed proving the system's reliability and the robust functionalities' performance. 
## The License
The license for this project is under the MIT License. For more enquires, See the LICENSE file 