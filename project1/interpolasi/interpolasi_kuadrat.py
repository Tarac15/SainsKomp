def interpolasi_kuadrat(x_points, y_points, x):
    if len(x_points) != 3 or len(y_points) != 3:
        raise ValueError("Interpolasi kuadrat memerlukan tepat 3 titik data.")

    x0, x1, x2 = x_points
    y0, y1, y2 = y_points

    L0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    L1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    L2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))

    return y0 * L0 + y1 * L1 + y2 * L2