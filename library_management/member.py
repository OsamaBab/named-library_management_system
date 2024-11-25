

class Member:
    """
    A class to represent a library member.

        Attributes:
        name : (str) The name of the member.
        borrowed_books : ([]) A list of books borrowed by the member.
    """

    def __init__(self, name):
        """
        Constructs and initialise all the necessary attributes for the member object.

        Parameters:
        name (str): The name of the member.
        borrowed_books : ([]) A list of books borrowed by the member.
        """
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Adds a book to the member's borrowed books list.

        Parameters:
        book (Book): The book to be borrowed.
        """
        self.borrowed_books.append(book)

    def return_book(self, book):
        """
        Removes a book from the member's borrowed books list.

        Parameters:
        book (Book): The book to be returned.
        """
        self.borrowed_books.remove(book)

class StudentMember(Member):
    """
    Description: 
    A class to represent a student member, inheriting from Member.

        Attributes:
        student_id : (str) The student ID of the member.
    """

    def __init__(self, name, student_id):
        """
        Description: 
        Constructs all the necessary attributes for the student member object.
            Parameters:
            name (str): The name of the student member.
            student_id (str): The student ID of the member.
        """
        super().__init__(name)
        self.student_id = student_id

class TeacherMember(Member):
    """
    Description: 
    A class to represent a teacher member, inheriting from Member.
        Attributes:
        teacher id : (str) The teacher ID of the member.
    """

    def __init__(self, name, teacher_id):
        """
        Description: 
        Constructs all the necessary attributes for the TeacherMember object.
            Parameters:
            name (str): The name of the teacher member.
            teacher_id (str): The teacher ID of the member.

        """
        super().__init__(name)
        self.teacher_id = teacher_id

    def __repr__(self):
        """
        Description: 
        For debugging purpose, this method Provides a string representation of the TeacherMember object.
            Returns:
            A formatted string to describe the teacher member.
        """
        return f"Teacher Member: {self.name}, ID: {self.teacher_id}"