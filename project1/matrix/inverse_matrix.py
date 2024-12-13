import numpy as np

def inverse_matrix():
    # Input matriks dari pengguna
    print("Masukkan elemen matriks A (dipisahkan dengan spasi untuk setiap elemen, baris baru untuk baris berikutnya):")
    rows_A = int(input("Masukkan jumlah baris matriks A: "))
    cols_A = int(input("Masukkan jumlah kolom matriks A: "))

    if rows_A != cols_A:
        print("Matriks harus persegi untuk dapat di-invers.")
    else:
        print(f"Masukkan elemen matriks A ukuran {rows_A}x{cols_A}:")
        A = []
        for i in range(rows_A):
            row = list(map(float, input(f"Baris {i+1}: ").split()))
            A.append(row)
        A = np.array(A)

        # Inversi matriks
        try:
            A_inv = np.linalg.inv(A)
            print("Inversi matriks A:\n", A_inv)
        except np.linalg.LinAlgError:
            print("Matriks A tidak dapat di-invers karena determinannya nol.")
