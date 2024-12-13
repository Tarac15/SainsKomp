import numpy as np

def multiplication_matrix():
    # Input matriks dari pengguna
    print("Masukkan elemen matriks A:")
    rows_A = int(input("Masukkan jumlah baris matriks A: "))
    cols_A = int(input("Masukkan jumlah kolom matriks A: "))

    print(f"Masukkan elemen matriks A ukuran {rows_A}x{cols_A}:")
    A = []
    for i in range(rows_A):
        row = list(map(float, input(f"Baris {i+1}: ").split()))
        A.append(row)
    A = np.array(A)

    print("Masukkan elemen matriks B:")
    rows_B = int(input("Masukkan jumlah baris matriks B: "))
    cols_B = int(input("Masukkan jumlah kolom matriks B: "))

    if cols_A != rows_B:
        print("Jumlah kolom matriks A harus sama dengan jumlah baris matriks B untuk perkalian.")
    else:
        print(f"Masukkan elemen matriks B ukuran {rows_B}x{cols_B}:")
        B = []
        for i in range(rows_B):
            row = list(map(float, input(f"Baris {i+1}: ").split()))
            B.append(row)
        B = np.array(B)

        # Perkalian matriks
        C = np.dot(A, B)
        print("Hasil perkalian matriks A dan B:\n", C)