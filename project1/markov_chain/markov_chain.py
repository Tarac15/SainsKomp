import numpy as np

def markov_chain():
    print("\n=== Metode Markov Chain ===")

    n = int(input("Masukkan ukuran matriks transisi (n x n): "))
    print("Masukkan elemen-elemen matriks transisi:")

    P = np.zeros((n, n))
    for i in range(n):
        P[i] = [float(x) for x in input(f"Baris {i + 1}: ").split()]

    # Periksa apakah matriks adalah matriks transisi yang valid
    if not np.allclose(P.sum(axis=1), 1):
        print("Matriks transisi tidak valid! Setiap baris harus memiliki total 1.")
        return

    # Masukkan vektor distribusi awal
    print("Masukkan distribusi awal (vektor probabilitas):")
    initial_state = np.array([float(x) for x in input().split()])

    if len(initial_state) != n or not np.isclose(initial_state.sum(), 1):
        print("Vektor distribusi awal tidak valid! Total harus 1 dan ukurannya sesuai dengan matriks transisi.")
        return

    # Iterasi untuk mencapai distribusi stasioner
    steps = int(input("Masukkan jumlah langkah iterasi: "))
    state = initial_state

    print("\nHasil tiap iterasi:")
    for step in range(steps):
        state = np.dot(state, P)
        print(f"Langkah {step + 1}: {state}")

    print("\nDistribusi Stasioner (perkiraan setelah iterasi):")
    print(state)