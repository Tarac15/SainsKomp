import numpy as np

def plus_minus_matrix():
    try:
        print("\n=== Penjumlahan dan Pengurangan Matriks ===")
        print("Fitur ini digunakan untuk menjumlahkan atau mengurangkan dua matriks.")

        # Input ukuran matriks
        rows = int(input("Masukkan jumlah baris matriks: "))
        cols = int(input("Masukkan jumlah kolom matriks: "))

        # Input matriks pertama
        print("Masukkan elemen-elemen Matriks A baris per baris:")
        A = []
        for i in range(rows):
            A.append(list(map(float, input(f"Baris {i+1}: ").split())))
        A = np.array(A)

        # Input matriks kedua
        print("Masukkan elemen-elemen Matriks B baris per baris:")
        B = []
        for i in range(rows):
            B.append(list(map(float, input(f"Baris {i+1}: ").split())))
        B = np.array(B)

        # Memastikan ukuran matriks sama
        if A.shape != B.shape:
            print("Penjumlahan atau pengurangan tidak dapat dilakukan karena ukuran matriks berbeda.")
            return

        # Memilih operasi
        print("Pilih operasi:")
        print("1. Penjumlahan (A + B)")
        print("2. Pengurangan (A - B)")
        choice = input("Masukkan pilihan (1/2): ")

        if choice == '1':
            result = A + B
            print("\nHasil penjumlahan Matriks (A + B):")
        elif choice == '2':
            result = A - B
            print("\nHasil pengurangan Matriks (A - B):")
        else:
            print("Pilihan tidak valid.")
            return

        print(result)

    except Exception as e:
        print("Terjadi kesalahan:", e)

    input("Tekan Enter untuk kembali ke menu utama.")