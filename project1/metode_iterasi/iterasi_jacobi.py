import numpy as np

def iterasi_jacobi(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for it in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, it + 1
        x = x_new
    return x, max_iter