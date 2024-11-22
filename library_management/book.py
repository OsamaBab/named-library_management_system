class Book:
    """
    A class to represent a book.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    """

    def __init__(self, title, author):
        """
        Constructs all the necessary attributes for the book object.
    
        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        available (boolean): The default availability for a book is True
        """
        self.title = title
        self.author = author
        self.available = True

    def __repr__(self):
        """
        A method represent the book class parameters
        Return:
        return a book title and author name
        """
        return f"Book Title: {self.title}, Author: {self.author}"
