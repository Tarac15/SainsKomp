import random
from sympy import symbols, sympify, lambdify

def monte_carlo():
    print("\n=== Metode Monte Carlo ===")

    # Input fungsi dan batas integral
    f_str = input("Masukkan fungsi f(x): ")
    a = float(input("Masukkan batas bawah (a): "))
    b = float(input("Masukkan batas atas (b): "))
    n = int(input("Masukkan jumlah titik acak (n): "))

    # Parsifikasi fungsi
    x = symbols('x')
    f = sympify(f_str)
    f_lambdified = lambdify(x, f)

    # Monte Carlo: Hitung integral
    random_points = [random.uniform(a, b) for _ in range(n)]
    total = sum(f_lambdified(xi) for xi in random_points)

    # Estimasi hasil integral
    integral = (b - a) * (total / n)
    print(f"Hasil estimasi integral menggunakan Monte Carlo: {integral:.6f}")