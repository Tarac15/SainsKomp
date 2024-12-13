import numpy as np
from scipy.linalg import lu, solve

def lu_decomposition():
    # Memasukkan ukuran matriks
    n = int(input("Masukkan ukuran matriks persegi A (n x n): "))

    # Input matriks A
    print(f"Masukkan elemen matriks A ukuran {n}x{n} (dipisahkan spasi per baris):")
    A = []
    for i in range(n):
        row = list(map(float, input(f"Baris {i + 1}: ").split()))
        A.append(row)
    A = np.array(A)

    # Input vektor b
    print(f"Masukkan elemen vektor b (dipisahkan spasi):")
    b = list(map(float, input().split()))
    b = np.array(b)

    # LU Decomposition
    P, L, U = lu(A)

    # Menampilkan matriks hasil LU decomposition
    print("\nMatriks A:\n", A)
    print("Matriks P (Permutation Matrix):\n", P)
    print("Matriks L (Lower Triangular Matrix):\n", L)
    print("Matriks U (Upper Triangular Matrix):\n", U)

    # Menyelesaikan sistem persamaan Ax = b
    x = solve(A, b)

    # Membulatkan solusi ke 10 desimal
    x = np.round(x, decimals=10)

    # Menampilkan solusi
    print("\nSolusi untuk [x1, x2, ..., xn]:\n", x)
