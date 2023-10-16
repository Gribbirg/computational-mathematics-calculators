def arif_round(x: float, value):
    if get_num(x, value + 1) == 5 and abs(round(x, value)) < abs(x):
        if x > 0:
            x += pow(10, -1 * value - 1)
        else:
            x -= pow(10, -1 * value - 1)
    return round(x, value)


def get_num(x, position):
    return int(abs(x * pow(10, position)) % 10)
