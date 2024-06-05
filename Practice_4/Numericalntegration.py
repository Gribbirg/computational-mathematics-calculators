from ForAll.ForAll import arif_round

A = 4
B = 12
C = -10
D = 9
E = -4
F = 3
G = -2
a = 1
b = 3
# тестовые границы с семинара
# a = -1.5
# b = 2
ROUND = 6

KOEF_TABLE = [[[-0.861136, 0.347854], [-0.339981, 0.652145],
               [0.339981, 0.652145], [0.861136, 0.347854]],
              [[-0.932464, 0.171324], [-0.661209, 0.360761], [-0.238619, 0.467913],
               [0.238619, 0.467913], [0.661209, 0.360761], [0.932464, 0.171324]],
              [[-0.960289, 0.101228], [-0.796666, 0.222381], [-0.525532, 0.313706], [-0.183434, 0.362683],
               [0.183434, 0.362683], [0.525532, 0.313706], [0.796666, 0.222381], [0.960289, 0.101228]]]

WAY_NAMES = ["LR", "PR", "MR", "Trapezoid", "Parabola", "Gauss"]


def fun(x):
    return arif_round((A * pow(x, 2) + B * x + C) / (D * pow(x, 3) + E * pow(x, 2) + F * x + G), ROUND)


# тестовая ф-ция с семинара
# def fun(x):
#     return arif_round(pow(x, 4) - x + 7, ROUND)


def get_h(n):
    return arif_round((b - a) / n, ROUND)


def left_rectangle(h, y_list):
    return arif_round(h * sum(y_list[:-1]), ROUND)


def right_rectangle(h, y_list):
    return arif_round(h * sum(y_list[1:]), ROUND)


def middle_rectangle(h, y_list):
    return arif_round(h * sum(y_list), ROUND)


def trapezoid(h, y_list):
    return arif_round(h * ((y_list[0] + y_list[-1]) / 2 + sum(y_list[1:-1])), ROUND)


def parabola(h, n, y_list):
    return arif_round(h / 3 * (y_list[0] + y_list[-1] + 2 * sum([y_list[2 * i] for i in range(1, n // 2)]) + 4 * sum(
        [y_list[2 * i + 1] for i in range(n // 2)])), ROUND)


def get_y_list(x_list):
    for i in x_list:
        print(f"f({i}) = {arif_round(fun(i), ROUND)}")
    return [arif_round(fun(i), ROUND) for i in x_list]


def get_y_gauss_list(n, x_list):
    print(f"f({(b + a) / 2} + {(b - a) / 2} * ({KOEF_TABLE[(n - 4) // 2][0][0]})) = f({x_list[0]}) = "
          f"{arif_round(fun(x_list[0]), ROUND)}")
    for i in range(1, n):
        print(f"f(- / - ({KOEF_TABLE[(n - 4) // 2][i][0]})) = f({x_list[i]}) = {arif_round(fun(x_list[i]), ROUND)}")
    return [arif_round(fun(i), ROUND) for i in x_list]


def gauss(n, y_list):
    return arif_round((b - a) / 2 * sum([KOEF_TABLE[(n - 4) // 2][i][1] * y_list[i] for i in range(n)]), ROUND)


def calculate(n):
    res = [0] * 6
    print("-" * 100)
    h = get_h(n)
    print(f"n = {n}\n\nh = {h}\n")

    x_list = [a]
    for _ in range(n):
        x_list.append(arif_round(x_list[len(x_list) - 1] + h, ROUND))

    print("base fun values:")
    y_list = get_y_list(x_list)
    print()

    res[0] = left_rectangle(h, y_list)
    res[1] = right_rectangle(h, y_list)
    res[3] = trapezoid(h, y_list)
    res[4] = parabola(h, n, y_list)
    print(f"left_rectangle: {res[0]}")
    print(f"right rectangle: {res[1]}")
    print(f"trapezoid: {res[3]}")
    print(f"parabola: {res[4]}")

    print("\nfun values for middle rectangle:")
    x_middle_list = [arif_round((x_list[i] + x_list[i + 1]) / 2, ROUND) for i in range(n)]
    y_middle_list = get_y_list(x_middle_list)
    print()
    res[2] = middle_rectangle(h, y_middle_list)
    print(f"middle_rectangle: {res[2]}")

    print("\nfun values for Gauss:")
    x_gauss_list = [arif_round((b + a) / 2 + (b - a) / 2 * KOEF_TABLE[(n - 4) // 2][i][0], ROUND) for i in range(n)]
    y_gauss_list = get_y_gauss_list(n, x_gauss_list)
    print()
    res[5] = gauss(n, y_gauss_list)
    print(f"Gauss: {res[5]}")

    return res


def print_table(t):
    print('%10s %30s' % ("Way", "Answer"))
    print('%10s %15d %15d %15d' % ("N", 4, 6, 8))
    for j in range(6):
        print('%10s %15f %15f %15f' % (WAY_NAMES[j], t[j][0], t[j][1], t[j][2]))


def create_pic(t):
    way = f"{A} {B} {C} {D} {E} {F} {G} {a} {b}"
    if "graphs" not in os.listdir():
        os.makedirs("graphs")
    if way not in os.listdir("graphs"):
        os.makedirs("graphs/" + way)

    way = "graphs/" + way
    plt.xlabel("N")
    plt.ylabel("I(N)")
    plt.plot([4, 6, 8], t[0], label=WAY_NAMES[0])
    plt.plot([4, 6, 8], t[1], label=WAY_NAMES[1])
    plt.plot([4, 6, 8], t[2], label=WAY_NAMES[2])
    plt.legend()
    plt.savefig(f"{way}/rectangles.png")
    plt.show()

    plt.xlabel("N")
    plt.ylabel("I (N)")
    plt.plot([4, 6, 8], t[3], label=WAY_NAMES[3])
    plt.plot([4, 6, 8], t[4], label=WAY_NAMES[4])
    plt.plot([4, 6, 8], t[5], label=WAY_NAMES[5])
    plt.legend()
    plt.savefig(f"{way}/other.png")
    plt.show()


table = [[0] * 3 for _ in range(6)]
for num in range(4, 9, 2):
    ans = calculate(num)
    for zn in range(6):
        table[zn][(num - 4) // 2] = ans[zn]

print("-" * 100)
print_table(table)
try:
    import matplotlib.pyplot as plt
    import os

    create_pic(table)
except ModuleNotFoundError:
    print(f"Can't create pictures: matplotlib.pyplot not founded")
