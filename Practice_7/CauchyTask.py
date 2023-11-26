from ForAll.ForAll import arif_round

A = 0.9
B = -2.1
# C = 0.5
C = 2

H = 0.5
FROM = 0
TO = 2
# ROUND = 6
ROUND = 8


# def fun(x, y):
#     return A * y + B * pow(x - 1, 2)

def fun(x, y):
    return pow(x, 2) + y


def euler(x, y):
    return arif_round(H * fun(x, y), ROUND)


def cauchy_euler(x, y):
    f = arif_round(fun(x, y), ROUND)
    print(f"fun({x}, {y}) = {f}")
    print(f"fun({x + H}, {y + H * fun(x, y)}) = {arif_round(fun(x + H, y + H * f), ROUND)}")
    return arif_round(H / 2 * (f + arif_round(fun(x + H, y + H * f), ROUND)), ROUND)


def runge_kutta(x, y):
    k = [arif_round(fun(x, y), ROUND)]
    print(f"k0 = {k[0]}")
    k.append(arif_round(fun(x + H / 2, y + H * k[0] / 2), ROUND))
    print(f"k1 = {k[1]}")
    k.append(arif_round(fun(x + H / 2, y + H * k[1] / 2), ROUND))
    print(f"k2 = {k[2]}")
    k.append(arif_round(fun(x + H, y + H * k[2]), ROUND))
    print(f"k3 = {k[3]}")
    return arif_round(H / 6 * (k[0] + 2 * k[1] + 2 * k[2] + k[3]), ROUND)


def get_table(delta_y_fun):
    ans = [[FROM, C]]
    x = FROM
    y = C
    i = 0
    print(f"x{i} = {x}, y{i} = {y}")
    while x + H <= TO:
        print()
        delta_y = delta_y_fun(x, y)
        y = arif_round(delta_y + y, ROUND)
        x += H
        ans.append([x, y])
        i += 1
        print(f"delta y = {delta_y}")
        print(f"x{i} = {x}, y{i} = {y}")
    print()
    return ans


def print_table(table):
    print("Answer:")
    print('%15s %15s' % ("x", "y"))
    for row in table:
        print('%15s %15s' % (row[0], row[1]))


print("Euler:")
print_table(get_table(euler))
print("-" * 100)

print("Cauchy-Euler:")
print_table(get_table(cauchy_euler))
print("-" * 100)

print("Runge_Kutta:")
print_table(get_table(runge_kutta))
print("-" * 100)
