class Matrix:
    """
    A class to represent a mathematical matrix and perform basic operations.

    Attributes:
        rows (int): Number of rows in the matrix.
        columns (int): Number of columns in the matrix.
        matrix (list of list of int): 2D list to store matrix elements.

    Methods:
        read():
            Reads matrix elements from user input.
        display():
            Displays the matrix in a formatted way.
        add(other):
            Returns a new Matrix that is the sum of self and other.
        sub(other):
            Returns a new Matrix that is the difference of self and other.
    """

    def __init__(self, rows: int, columns: int):
        """
        Initializes a Matrix object with the given number of rows and columns.

        Args:
            rows (int): Number of rows.
            columns (int): Number of columns.
        """
        self.rows = rows
        self.columns = columns
        self.matrix = []

    def read(self):
        """
        Reads matrix elements from user input and fills the matrix.

        Returns:
            int: 1 after successful input.
        """
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(int(input(f"Enter element at position ({i+1}, {j+1}): ")))
            self.matrix.append(row)
        return 1

    def display(self):
        """
        Displays the matrix in a formatted way.

        Returns:
            int: 1 after displaying the matrix.
        """
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.matrix[i][j], end=" ")
            print()
        return 1

    def __add__(self, other):
        """
        Adds two matrices of the same dimensions.

        Args:
            other (Matrix): The matrix to add.

        Returns:
            Matrix: A new Matrix object containing the sum.

        Raises:
            SystemExit: If the dimensions do not match.
        """
        if self.rows != other.rows or self.columns != other.columns:
            print("Don't know much about matrix, eh?")
            exit(1)
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(int(self.matrix[i][j]) + int(other.matrix[i][j]))
            result.matrix.append(row)
        return result

    def __sub__(self, other):
        """
        Subtracts another matrix from this matrix.

        Args:
            other (Matrix): The matrix to subtract.

        Returns:
            Matrix: A new Matrix object containing the difference.

        Raises:
            SystemExit: If the dimensions do not match.
        """
        if self.rows != other.rows or self.columns != other.columns:
            print("Don't know much about matrix, eh?")
            exit(1)
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(int(self.matrix[i][j]) - int(other.matrix[i][j]))
            result.matrix.append(row)
        return result
    def __mul__(self, other):
        """
            Multiplies two matrices.

            Args:
                other (Matrix): The matrix to multiply with.

            Returns:
                Matrix: A new Matrix object containing the product.

            Raises:
                SystemExit: If the matrix dimensions are incompatible for multiplication.
        """
        if self.columns != other.rows or self.rows != other.columns:
            print("Don't know much about matrix, eh?")
            exit(1)
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            templ = []
            for j in range(other.columns):
                temp = 0.0
                for k in range(self.columns):
                    temp += self.matrix[i][k] * other.matrix[k][j]
                templ.append(temp)
            result.matrix.append(templ)
        return result
new = Matrix(2,2)
new.read()
new.display()
new+=new
new.display()
new*=new
new.display()
            
