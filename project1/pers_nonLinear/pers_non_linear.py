from pers_nonLinear.table_method import table_method
from pers_nonLinear.biseksi_method import biseksi_method
from pers_nonLinear.secant_method import secant_method
from pers_nonLinear.newton_raphson_method import newton_raphson_method
from pers_nonLinear.regula_falsi_method import regula_falsi_method
from pers_nonLinear.simple_iteration_method import simple_iteration_method

import numpy as np
from sympy import sympify, lambdify, Symbol, diff

def get_function():

    x = Symbol('x')
    while True:
        try:
            func_str = input("Masukkan fungsi f(x) (contoh: x**3 - 6*x**2 + 11*x - 6): ")
            func_sympy = sympify(func_str)  # Konversi string menjadi ekspresi SymPy
            f = lambdify(x, func_sympy, modules=["numpy"])  # Konversi menjadi fungsi Python
            return f, func_sympy
        except Exception as e:
            print(f"Kesalahan dalam fungsi: {e}. Coba lagi.")

def pers_non_linear():

    print("\nMasukkan fungsi untuk diselesaikan:")
    f, func_sympy = get_function()  # Dapatkan fungsi dari pengguna

    while True:
        print("\n=== Penyelesaian Pers. non Linear ===")
        print("1. Metode Tabel")
        print("2. Metode Biseksi")
        print("3. Metode Regula Falsi")
        print("4. Metode Iterasi Sederhana")
        print("5. Metode Newton-Raphson")
        print("6. Metode Secant")
        print("0. Kembali ke Menu Utama")

        try:
            choice = int(input("Masukkan Pilihan: "))
            if choice == 1:
                a = float(input("Masukkan batas bawah (a): "))
                b = float(input("Masukkan batas atas (b): "))
                dx = float(input("Masukkan langkah pencarian (dx): "))

                tabel, akar = table_method(f, a, b, dx)
                print("\nTabel Nilai:")
                print(tabel)
                print("\nInterval Akar:")
                if akar:
                    for interval in akar:
                        print(f"Akar ditemukan di sekitar: {interval}")
                else:
                    print("Tidak ada akar yang ditemukan dalam rentang ini.")

            elif choice == 2:
                a = float(input("Masukkan batas bawah (a): "))
                b = float(input("Masukkan batas atas (b): "))
                tol = float(input("Masukkan toleransi (tol): "))

                try:
                    akar_biseksi, iterasi = biseksi_method(f, a, b, tol)
                    print(f"\nAkar ditemukan: {akar_biseksi} (ditemukan dalam {iterasi} iterasi)")
                except ValueError as e:
                    print(f"Kesalahan: {e}")

            elif choice == 3:
                a = float(input("Masukkan batas bawah (a): "))
                b = float(input("Masukkan batas atas (b): "))
                tol = float(input("Masukkan toleransi (tol): "))

                try:
                    akar_regula, iterasi = regula_falsi_method(f, a, b, tol)
                    print(f"\nAkar ditemukan: {akar_regula} (ditemukan dalam {iterasi} iterasi)")
                except ValueError as e:
                    print(f"Kesalahan: {e}")

            elif choice == 4:
                g_str = input("Masukkan fungsi iterasi g(x): ")
                g_sympy = sympify(g_str)
                g = lambdify(Symbol('x'), g_sympy, modules=["numpy"])
                x0 = float(input("Masukkan nilai awal (x0): "))
                tol = float(input("Masukkan toleransi (tol): "))
                max_iter = int(input("Masukkan iterasi maksimum: "))

                try:
                    akar_iterasi, iterasi = simple_iteration_method(f, g, x0, tol, max_iter)
                    print(f"\nAkar ditemukan: {akar_iterasi} (ditemukan dalam {iterasi} iterasi)")
                except ValueError as e:
                    print(f"Kesalahan: {e}")

            elif choice == 5:
                x0 = float(input("Masukkan nilai awal (x0): "))
                tol = float(input("Masukkan toleransi (tol): "))
                max_iter = int(input("Masukkan iterasi maksimum: "))

                df = diff(func_sympy, Symbol('x'))
                df_func = lambdify(Symbol('x'), df, modules=["numpy"])

                try:
                    akar_newton, iterasi = newton_raphson_method(f, df_func, x0, tol, max_iter)
                    print(f"\nAkar ditemukan: {akar_newton} (ditemukan dalam {iterasi} iterasi)")
                except ValueError as e:
                    print(f"Kesalahan: {e}")

            elif choice == 6:
                x0 = float(input("Masukkan nilai awal pertama (x0): "))
                x1 = float(input("Masukkan nilai awal kedua (x1): "))
                tol = float(input("Masukkan toleransi (tol): "))
                max_iter = int(input("Masukkan iterasi maksimum: "))

                try:
                    akar_secant, iterasi = secant_method(f, x0, x1, tol, max_iter)
                    print(f"\nAkar ditemukan: {akar_secant} (ditemukan dalam {iterasi} iterasi)")
                except ValueError as e:
                    print(f"Kesalahan: {e}")

            elif choice == 0:
                print("Kembali ke menu utama.")
                break

            else:
                print("Pilihan tidak valid, coba lagi.")

        except ValueError as e:
            print(f"Kesalahan input: {e}. Coba lagi.")

