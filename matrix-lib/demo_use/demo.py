from Matrix import Matrix

A=Matrix([[1 ,2 ,3 ], [2 ,3 ,4 ], [4 ,5 ,6 ]])
B=Matrix([[7 ,5 ,3 ], [2 ,9 ,0 ],[8 ,6 ,4]])
c=10

print("A:")
print(A)
print("\nB:")
print(B)
print("c:")
print(c)

print("\nA + B:")
print(A.add(B))

print("\nA-B")
print(A.subtract(B))

print("\nA'")
print(A.transpose())

print("\nA*B")
print(A.multiply(B))

print("\nA*c")
print(A.scalar_multiply(c))

print("\nTrace(A)")
print(A.trace())

print("\nMatrice identitate de dimensiune c")
print(Matrix.identity(c))

print("\nMatrice superior triunghiulara  A")
print(A.toUpper()[0])
#retruneaza si numarul de interschimbari daca le face intrun singur tuplu
#si doar accesez elementul care ma intereseaza
#e comod pentru calcularea determinantului

print("\nMatrice inferior triunghiulara  A")
print(A.toLower()[0])

print("\nDeterminantul matricii A")
print(d.det())
