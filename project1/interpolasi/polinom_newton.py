def polinom_newton(x_points, y_points, x):
    n = len(x_points)
    divided_diff = [[0 for _ in range(n)] for _ in range(n)]

    # Mengisi tabel selisih terbagi
    for i in range(n):
        divided_diff[i][0] = y_points[i]

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (x_points[i + j] - x_points[i])

    # Menghitung nilai interpolasi
    result = divided_diff[0][0]
    for i in range(1, n):
        term = divided_diff[0][i]
        for j in range(i):
            term *= (x - x_points[j])
        result += term

    return result