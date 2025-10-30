from Matrix import Matrix

def test_addition():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[1, 1], [1, 1]])
    C = A.add(B)
    assert C.data == [[2, 3], [4, 5]]
def test_sutraction():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[1, 1], [1, 1]])
    C = A.subtract(B)
    assert C.data == [[0, 1], [2, 3]]
def test_multiply():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[1, 1], [1, 1]])
    C = A.multiply(B)
    assert C.data == [[3, 3], [7, 7]]
def test_scalar_multiply():
    A = Matrix([[1, 2], [3, 4]])
    B = 3
    C = A.scalar_multiply(B)
    assert C.data ==[[3, 6],[9, 12]]
def test_trace():
    A = Matrix([[1, 2], [3, 4]])
    B=A.trace()
    assert B==5
    def test_Upper():
    A = Matrix([[1, 2, 3], [2, 3, 4], [4, 5, 6]])
    B=A.toUpper()
    assert B.data==[[1, 2, 3,],[0.0, -1.0, -2.0],[0.0, 0.0, 0.0]]
