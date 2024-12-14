def lcg():
    print("\n=== Linear Congruential Generator (LCG) ===")
    try:
        seed = int(input("Masukkan nilai awal (seed): "))
        a = int(input("Masukkan faktor pengali (a): "))
        c = int(input("Masukkan nilai increment (c): "))
        m = int(input("Masukkan nilai modulus (m): "))
        n = int(input("Masukkan jumlah bilangan pseudo-random yang diinginkan: "))

        # Fungsi untuk menghasilkan bilangan pseudo-random
        def generate_lcg(seed, a, c, m, n):
            current = seed
            random_numbers = []
            for _ in range(n):
                current = (a * current + c) % m
                random_numbers.append(current)
            return random_numbers

        # Panggil fungsi generate_lcg
        random_numbers = generate_lcg(seed, a, c, m, n)
        print("\nBilangan pseudo-random yang dihasilkan:")
        print(random_numbers)
    except ValueError:
        print("Masukkan nilai numerik yang valid!")