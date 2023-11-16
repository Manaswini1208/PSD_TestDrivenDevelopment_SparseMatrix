from sparse_recommender import SparseMatrix

def test_set():
    matrix = SparseMatrix()
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(1, 1, 0)
    matrix.set(1, 0, 2)
    assert matrix.get(0, 0) == 1
    assert matrix.get(0, 1) == 2
    assert matrix.get(1, 1) == 0
    assert matrix.get(1, 0) == 2

def test_get():
    matrix = SparseMatrix()
    assert matrix.get(0, 0) == 0
    matrix.set(1,1,6)
    matrix.set(2,2,8)
    assert matrix.get(1, 1) == 6
    assert matrix.get(2,2) == 8

def test_recommend():
    matrix = SparseMatrix()
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0,2, 3)
    matrix.set(1,0,4)
    matrix.set(1,1,5)
    matrix.set(1,2,6)
    matrix.set(2, 0, 7)
    matrix.set(2, 1, 8)
    matrix.set(2, 2, 9)

    matrix1 = SparseMatrix()
    matrix1.set(0,0,5)
    matrix1.set(1,1,8)


    vector = [3,1,2]
    vector1 = [1,2]
    result = matrix.recommend(vector)
    result1 = matrix1.recommend(vector1)
    assert result == [11,29,47]
    assert result1 == [5,16]

def test_add_movie():
    matrix1 = SparseMatrix()
    matrix1.set(0, 0, 1)
    matrix1.set(0, 1, 2)
    matrix1.set(1, 0, 3)

    matrix2 = SparseMatrix()
    matrix2.set(0, 1, 4)
    matrix2.set(1, 1, 5)

    result_matrix = matrix1.add_movie(matrix2)
    assert result_matrix.get(0, 0) == 1
    assert result_matrix.get(0, 1) == 4
    assert result_matrix.get(1, 0) == 3
    assert result_matrix.get(1, 1) == 5

def test_to_dense():
    matrix1 = SparseMatrix()
    matrix1.set(0,0,3)
    matrix1.set(0,2,4)
    matrix1.set(1,0,2)
    matrix1.set(1,2,6)
    matrix1.set(2,1,5)
    matrix1.set(2,2,8)
    dense_matrix = matrix1.to_dense()

    assert dense_matrix == [[3, 0,4], [2, 0,6], [0, 5,8]]

if __name__ == "__main__":
    test_set()
    test_get()
    test_recommend()
    test_add_movie()
    test_to_dense()
    print("All tests passed!")
