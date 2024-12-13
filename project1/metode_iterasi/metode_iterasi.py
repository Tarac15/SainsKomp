from metode_iterasi.iterasi_jacobi import iterasi_jacobi
from metode_iterasi.iterasi_gauss_seidel import iterasi_gauss_seidel

import numpy as np

def input_matriks_vektor():
    n = int(input("Masukkan jumlah variabel (n): "))
    print("Masukkan elemen matriks A (dalam baris):")
    A = np.array([list(map(float, input(f"Baris {i + 1}: ").split())) for i in range(n)])
    print("Masukkan elemen vektor b:")
    b = np.array([float(input(f"b[{i + 1}]: ")) for i in range(n)])
    return A, b

def metode_iterasi():
    # Input matriks dan vektor
    A, b = input_matriks_vektor()
    n = len(A)

    # Input tambahan
    x0 = np.zeros(n)  # Solusi awal, diasumsikan nol
    tol = float(input("Masukkan toleransi (contoh: 1e-6): "))
    max_iter = int(input("Masukkan jumlah iterasi maksimum: "))

    while True:  # Ganti dengan True (huruf besar)
        print("\n=== Penyelesaian Pers. Non Linear ===")
        print("1. Iterasi Jacobi")
        print("2. Iterasi Gauss Seidel")
        print("3. Keluar")  # Opsi untuk keluar dari loop

        try:
            choice = int(input("Masukkan pilihan: "))
            if choice == 1:
                # Metode Jacobi
                print("\n=== Metode Iterasi Jacobi ===")
                x_jacobi, iter_jacobi = iterasi_jacobi(A, b, x0, tol, max_iter)  # Gunakan fungsi yang sudah diimpor
                print(f"Hasil solusi: {x_jacobi}")
                print(f"Jumlah iterasi: {iter_jacobi}")
            elif choice == 2:  # Gunakan == untuk perbandingan
                # Metode Gauss-Seidel
                print("\n=== Metode Iterasi Gauss-Seidel ===")
                x_gs, iter_gs = iterasi_gauss_seidel(A, b, x0, tol, max_iter)  # Gunakan fungsi yang sudah diimpor
                print(f"Hasil solusi: {x_gs}")
                print(f"Jumlah iterasi: {iter_gs}")
            elif choice == 3:
                print("Keluar dari program.")
                break  # Keluar dari while loop
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Masukkan pilihan yang valid (angka).")
