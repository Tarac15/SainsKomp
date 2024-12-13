from matrix.solve_matrix import solve_matrix
from pers_nonLinear.pers_non_linear import pers_non_linear
from metode_iterasi.metode_iterasi import metode_iterasi
from interpolasi.interpolasi import interpolasi
from markov_chain.markov_chain import markov_chain
from simulasi_montecarlo.simulasi_montecarlo import simulasi_montecarlo

def main_menu():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Matriks")
        print("2. Persamaan non-linear")
        print("3. Metode Iterasi")
        print("4. Polinomial")
        print("5. Markov Chain")
        print("6. Monte Carlo")
        print("0. Keluar")

        try:
            choice = int(input("Pilih menu: "))
            if choice == 1:
                solve_matrix()
            elif choice == 2:
                pers_non_linear()
            elif choice == 3:
                metode_iterasi()
            elif choice == 4:
                interpolasi()
            elif choice == 5:
                markov_chain()
            elif choice == 6:
                simulasi_montecarlo()
            elif choice == 0:
                print("Keluar dari program. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid!")

if __name__ == "__main__":
    main_menu()