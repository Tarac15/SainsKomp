import numpy as np

def iterasi_gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for it in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, it + 1
        x = x_new
    return x, max_iter