class SparseMatrix:
    def __init__(self):
        #Dictionary to store non-zero elements as sparse matrix.
        self.dictionary = {}

    def set(self, row, col, value):
        # Sets the value at (row, col) to value.
        if row < 0 or col < 0:
            raise ValueError("Please specify non-negative indices for rows and column.")
        if not isinstance(value, (int, float)) or not isinstance(col, int) or not isinstance(row,int):
            raise ValueError("Indices must be integers and value should be of type int.")
        #sets the value in the sparse matrix if it is not zero.
        if value != 0:
            self.dictionary[(row, col)] = value
        elif (row, col) in self.dictionary:
            # del self.dictionary[(row, col)]
            self.dictionary.pop((row, col), None)
            # Remove zero values to keep the matrix sparse


#This method returns the value at specified index.
    def get(self, row, col):
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("Please specify integer indices for rows and columns.")
        if row < 0 or col < 0:
            raise ValueError("Please specify non-negative indices for rows and columns.")
        return self.dictionary.get((row, col), 0)


#To add given vector to the sparse matrix.
    def recommend(self, vector):
        # Multiplies the sparse matrix with a given vector to produce recommendations and returns the result.
        recommendedVector = []
        if not isinstance(vector, list) or not all(isinstance(x, (int, float)) for x in vector):
            raise ValueError("Vector should contain numbers.")
        if len(vector) != len(set(row for row, _ in self.dictionary.keys())):
            raise ValueError("length of columns and vector should be same.")
        for i in range(len(vector)):
            #Adding the elements in the sparse matrix to the elements in the vector row wise.
            recommendation = sum(self.get(i, j) * vector[j] for j in range(len(vector)))
            recommendedVector.append(recommendation)
        return recommendedVector

#This method adds another sparsematrixand generates a new movie to the service.
    def add_movie(self, matrix):
        if not isinstance(matrix, SparseMatrix):
            raise ValueError("Matrix should be of type sparseMatrix")
        newMovieService = SparseMatrix()
        for (row, col), value in self.dictionary.items():
            newMovieService.set(row, col, value)
        for (row, col), value in matrix.dictionary.items():
            newMovieService.set(row, col, value)
        return newMovieService

    #To convert sparse matrix to dense matrix.

    def to_dense(self):
        maximumRow = max(row for row, _ in self.dictionary.keys())
        maximumCol = max(col for _, col in self.dictionary.keys())

        #Creating a dense matrix
        dense_matrix = [[0 for _ in range(maximumCol + 1)] for _ in range(maximumRow + 1)]

        # To fill the non-zero values from dictionary
        for (row, col), value in self.dictionary.items():
            dense_matrix[row][col] = value

        return dense_matrix
