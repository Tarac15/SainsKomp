from simulasi_montecarlo.monte_carlo import monte_carlo
from simulasi_montecarlo.montecarlo_pi import montecarlo_pi

def simulasi_montecarlo():
    while True:
        print("\n=== Monte Carlo ===")
        print("1. Simulasi Monte Carlo")
        print("2. montecarlo_pi")
        print("0. Kembali ke Menu Utama")

        try:
            choice = int(input("Masukkan Pilihan: "))
            if choice == 1:
                monte_carlo()
            elif choice == 2:
                montecarlo_pi()
            elif choice == 0:
                break
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid!")