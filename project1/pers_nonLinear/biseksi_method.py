def biseksi_method(f, a, b, tol):

    if f(a) * f(b) >= 0:
        raise ValueError("Fungsi tidak berubah tanda pada interval [a, b].")

    iterasi = 0
    while (b - a) / 2 > tol:
        iterasi += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c, iterasi
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2, iterasi