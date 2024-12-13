import numpy as np


def gauss_elimination():
    print("\n=== Eliminasi Gauss ===")
    try:
        # Input jumlah variabel
        n = int(input("Masukkan jumlah variabel: "))

        # Input matriks augmented
        print("Masukkan elemen matriks augmented (A|B):")
        augmented_matrix = []
        for i in range(n):
            row = list(map(float, input(f"Baris {i + 1}: ").split()))
            augmented_matrix.append(row)
        augmented_matrix = np.array(augmented_matrix)

        # Proses eliminasi
        for i in range(n):
            # Pivoting: Memastikan diagonal utama tidak nol
            if augmented_matrix[i, i] == 0:
                for k in range(i + 1, n):
                    if augmented_matrix[k, i] != 0:
                        augmented_matrix[[i, k]] = augmented_matrix[[k, i]]  # Tukar baris
                        break
                else:
                    raise ValueError("Matriks tidak memiliki solusi unik.")

            # Normalisasi baris pivot
            pivot = augmented_matrix[i, i]
            augmented_matrix[i] = augmented_matrix[i] / pivot

            # Eliminasi elemen di bawah diagonal
            for j in range(i + 1, n):
                factor = augmented_matrix[j, i]
                augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]

        # Back substitution untuk menemukan solusi
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i + 1:n], x[i + 1:n])

        print("\nSolusi (x):")
        print(x)

    except Exception as e:
        print("Terjadi kesalahan:", e)

    input("\nTekan Enter untuk kembali ke menu utama.")
