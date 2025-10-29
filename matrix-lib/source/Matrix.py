"""
O mini biblioteca de operatii pe matrici structurate intrun singur proiect
__________________________________________________________________________
Autor: Andrei Botnari
Facultatea De Matematica UAIC, IAȘI
"""
class Matrix:
    """
    Clasă pentru operații de bază cu matrici (adunare, înmulțire, determinant etc.)
    """

    def __init__(self, data):
        """
        Verificăm dacă matricea este validă: listă de liste cu aceeași dimensiune.
        """
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Toate liniile ar trebui să aibă aceeași dimensiune")

        self.data = data
        self.row = len(data)
        self.cols = len(data[0])

    def __str__(self):
        """
        Reprezentare pentru print()
        """
        return "\n".join([" ".join(map(str,row)) for row in self.data])

    def add(self, other):
        """
        Operatia de adunare pe matrici
        """
        if self.row != other.row or self.cols != other.cols:
            raise ValueError("Matricile sunt incompatibile dupa dimensiune")
        result = [
            [self.data[i][j]+other.data[i][j] for j in range(self.cols)] for i in range(self.row)
        ]
        return Matrix(result)

    def subtract(self, other):
        """
        Scaderea matricilor
        """
        if self.row!=other.row or self.cols!=other.cols:
            raise ValueError("matrci incompatibile pentru scadere")
        result =[
            [self.data[i][j]- other.data[i][j] for j in range(self.cols)]
            for i in range(self.row)
        ]
        return Matrix(result)

    def transpose(self):
        """
        Transpusa unei matrici
        """
        result =[
            [self.data[j][i] for j in range(self.row)] for i in range(self.cols)
        ]
        return Matrix(result)

    def multiply(self, other):
        """
        Înmulțirea matricilor
        """
        if self.cols != other.row:
            raise ValueError("Matrici incompatibile")
        result=[
            [sum(self.data[i][k]*other.data[k][j] for k in range(self.row))
             for j in range(other.cols)]
            for i in range(self.row)
        ]
        return Matrix(result)

    def scalar_multiply(self, data):
        """
        Inmultire cu un scalar
        """
        result = [
            [self.data[i][j]*data for j in range(self.cols)]
            for i in range(self.row)
        ]
        return Matrix(result)

    def trace(self):
        """
        Urma unei matrici
        """
        result = sum(self.data[i][i] for i in range(self.row))
        return result

    def identity(n):
        """
        Returneaza Matricea identitate
        """
        result = [
            [1 if j==i else 0 for j in range(n)]
            for i in range(n)
        ]
        return Matrix(result)
