def newton_raphson_method(f, df, x0, tol, max_iter):

    iterasi = 0
    x = x0
    while iterasi < max_iter:
        iterasi += 1
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new, iterasi
        x = x_new
    raise ValueError("Iterasi maksimum tercapai tanpa konvergensi.")