import numpy as np
import pandas as pd

def table_method(f, a, b, dx):

    x_values = np.arange(a, b + dx, dx)
    y_values = f(x_values)

    tabel = pd.DataFrame({
        'x': x_values,
        'f(x)': y_values
    })

    akar = []
    for i in range(len(y_values) - 1):
        if y_values[i] * y_values[i + 1] < 0:
            akar.append((x_values[i], x_values[i + 1]))

    return tabel, akar