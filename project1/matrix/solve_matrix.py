from matrix.lu_decomposition import lu_decomposition
from matrix.plus_minus_matrix import plus_minus_matrix
from matrix.gauss_elimination import gauss_elimination
from matrix.inverse_matrix import inverse_matrix
from matrix.multiplication_matrix import multiplication_matrix

def solve_matrix():
    while True:
        print("\n=== Penyelesaian Matriks ===")
        print("1. Penjumlahan dan Pengurangan Matriks")
        print("2. Eliminasi Gauss")
        print("3. Inverse Matriks")
        print("4. Perkalian Matriks")
        print("5. LU Decomposition")
        print("0. Kembali ke Menu Utama")

        try:
            choice = int(input("Masukkan Pilihan: "))
            if choice == 1:
                plus_minus_matrix()
            elif choice == 2:
                gauss_elimination()
            elif choice == 3:
                inverse_matrix()
            elif choice == 4:
                multiplication_matrix()
            elif choice == 5:
                lu_decomposition()
            elif choice == 0:
                break
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid!")