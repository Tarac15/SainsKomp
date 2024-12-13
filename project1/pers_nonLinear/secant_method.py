def secant_method(f, x0, x1, tol, max_iter):

    iterasi = 0
    while iterasi < max_iter:
        iterasi += 1
        if f(x1) - f(x0) == 0:
            raise ValueError("Pembagian dengan nol terjadi pada iterasi ke-{iterasi}.")
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x_new - x1) < tol:
            return x_new, iterasi
        x0, x1 = x1, x_new
    raise ValueError("Iterasi maksimum tercapai tanpa konvergensi.")