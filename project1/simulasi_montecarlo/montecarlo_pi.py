import random

def montecarlo_pi():
    print("\n=== Simulasi Monte Carlo: Menghitung Nilai Pi ===")

    # Input jumlah titik acak
    n = int(input("Masukkan jumlah titik acak (n): "))

    # Hitung titik di dalam lingkaran menggunakan list comprehension
    inside_circle = sum(
        1 for _ in range(n) if random.uniform(-1, 1) ** 2 + random.uniform(-1, 1) ** 2 <= 1
    )

    # Estimasi nilai Pi
    pi_estimate = (inside_circle / n) * 4
    print(f"Estimasi nilai Pi berdasarkan {n} titik acak adalah: {pi_estimate:.6f}")