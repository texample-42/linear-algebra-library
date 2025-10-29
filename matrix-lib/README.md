# 🧮 Matrix Mini Library

O mini-bibliotecă scrisă în Python pentru operații de bază și/sau operații mai avansate pe matrici.  
Proiect educațional realizat ca exercițiu practic pentru cursurile de **Algebră Liniară** și **Fundamentele Programării**, UAIC Iași.

---

## 🚀 Funcționalități
- ✅ Adunare/Scîdere de matrici
- ✅ Transpusă
- ✅ Înmulțire matricială
- ✅ Urma matricii
- ✅ Matrici identitate
- ⚙️ Verificări pentru dimensiuni compatibile

---

## 😶‍🌫️În curând...
-Înmulțire matrice-vector
-Transpunere matrice
-Calcul rang matrice

-Descompunere LU
-Descompunere QR
-Valori proprii și vectori proprii
-Descompunere SVD

-Operații cu matrice rare
-Suport pentru numere complexe
-Optimizări pentru performanță
-Interfață Python

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🧠 Exemple
```python
from src.matrix import Matrix

A = Matrix([[1,2],[3,4]])
B = Matrix([[5,6],[7,8]])

print("A + B:")
print(A.add(B))


