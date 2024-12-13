from interpolasi.interpolasi_linear import interpolasi_linear
from interpolasi.interpolasi_kuadrat import interpolasi_kuadrat
from interpolasi.polinom_newton import polinom_newton

def interpolasi():
    while True:
        print("\n=== Penyelesaian Interpolasi ===")
        print("1. Interpolasi Linear")
        print("2. Interpolasi Kuadrat")
        print("3. Polinom Newton")
        print("0. Kembali ke Menu Utama")

        try:
            choice = int(input("Masukkan Pilihan: "))
            if choice == 1:
                print("\n-- Interpolasi Linear --")
                x0 = float(input("Masukkan x0: "))
                y0 = float(input("Masukkan y0: "))
                x1 = float(input("Masukkan x1: "))
                y1 = float(input("Masukkan y1: "))
                x = float(input("Masukkan nilai x yang ingin diinterpolasi: "))
                y = interpolasi_linear(x0, y0, x1, y1, x)
                print(f"Hasil interpolasi linear untuk x={x} adalah y={y}")

            elif choice == 2:
                print("\n-- Interpolasi Kuadrat --")
                x_points = [float(input(f"Masukkan x{i}: ")) for i in range(3)]
                y_points = [float(input(f"Masukkan y{i}: ")) for i in range(3)]
                x = float(input("Masukkan nilai x yang ingin diinterpolasi: "))
                y = interpolasi_kuadrat(x_points, y_points, x)
                print(f"Hasil interpolasi kuadrat untuk x={x} adalah y={y}")

            elif choice == 3:
                print("\n-- Polinom Newton --")
                n = int(input("Masukkan jumlah titik data: "))
                x_points = [float(input(f"Masukkan x{i}: ")) for i in range(n)]
                y_points = [float(input(f"Masukkan y{i}: ")) for i in range(n)]
                x = float(input("Masukkan nilai x yang ingin diinterpolasi: "))
                y = polinom_newton(x_points, y_points, x)
                print(f"Hasil polinom Newton untuk x={x} adalah y={y}")

            elif choice == 0:
                print("Kembali ke menu utama.")
                break

            else:
                print("Pilihan tidak valid, coba lagi.")

        except ValueError:
            print("Masukkan angka yang valid!")
