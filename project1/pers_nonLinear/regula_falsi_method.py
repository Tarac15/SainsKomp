def regula_falsi_method(f, a, b, tol):

    if f(a) * f(b) >= 0:
        raise ValueError("Fungsi tidak berubah tanda pada interval [a, b].")

    iterasi = 0
    c = a
    while abs(f(c)) > tol:
        iterasi += 1
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, iterasi