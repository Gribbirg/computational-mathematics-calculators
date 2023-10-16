from ForAll.ForAll import arif_round


# ENTER THIS ____________________________________________________________________________________________


K = float(input("K = "))
L = float(input("L = "))
# _______________________________________________________________________________________________________

E = 0.006
ROUND_TO_NUM = 3
ROUND_TO_CALC = 4


def fun(x):
    return arif_round(pow(x, 3) - K * x - L, ROUND_TO_CALC)


def derivative(x):
    return arif_round(3 * pow(x, 2) - K, ROUND_TO_CALC)


def second_derivative(x):
    return arif_round(6 * x, ROUND_TO_CALC)


def check(x, function):
    sym = "g" if function == derivative else "f"
    plus = function(x + E)
    minus = function(x - E)
    print(f"{sym}({arif_round(x + E, 7)}) = {plus}; {sym}({arif_round(x - E, 7)}) = {minus}")
    return checking_for_different(plus, minus)


def checking_for_different(a, b):
    return a < 0 < b or a > 0 > b


def half_division_method(a: float, b: float, i=1):
    print(f"\n{i}:")
    c = arif_round((a + b) / 2, ROUND_TO_NUM)
    print(f"a = {a}; b = {b}; g(a) = {derivative(a)}; g(b) = {derivative(b)}; c = {c}; g(c) = {derivative(c)}")
    if check(c, derivative):
        return c
    else:
        if checking_for_different(derivative(a), derivative(c)):
            return half_division_method(a, c, i + 1)
        else:
            return half_division_method(c, b, i + 1)


def chord_method(a: float, b: float, i=1):
    print(f"\n{i}:")
    x = arif_round(a - (fun(a) * (b - a)) / (fun(b) - fun(a)), ROUND_TO_NUM)
    print(f"a = {a}; b = {b}; f(a) = {fun(a)}; f(b) = {fun(b)}; x = {x}; fun(x) = {fun(x)}")
    if check(x, fun):
        return x
    else:
        if checking_for_different(fun(a), fun(x)):
            return chord_method(a, x, i + 1)
        else:
            return chord_method(x, b, i + 1)


def secant_method(x1_pred: float, x2_pred: float, i=1):
    print(f"\n{i}:")
    x = arif_round(x1_pred - (fun(x1_pred) * (x1_pred - x2_pred)) / (fun(x1_pred) - fun(x2_pred)), ROUND_TO_NUM)
    print(f"x = {x}; fun(x) = {fun(x)}")
    if check(x, fun):
        return x
    else:
        return secant_method(x, x1_pred, i + 1)


def simple_iteration_method(x_pred: float, k=0, i=0):
    if i == 0:
        k = arif_round((B - A) / (derivative(B) - derivative(A)), ROUND_TO_NUM)
        print(f"k = {k}")
        print(f"\n0:")
        print(f"x = A = {A}; g({A}) = {derivative(A)}")
        return simple_iteration_method(x_pred, k, 1)
    print(f"\n{i}:")
    x = arif_round(x_pred - derivative(x_pred) * k, ROUND_TO_NUM)
    print(f"x = {x}; g({x}) = {derivative(x)}")
    if check(x, derivative):
        return x
    else:
        return simple_iteration_method(x, k, i + 1)


def tangent_method(x_pred: float = 0, i=0):
    if i == 0:
        if not checking_for_different(fun(A), second_derivative(A)):
            print(f"start from A = {A}, fun(A) = {A} derivative(A) = {derivative(A)}")
            return tangent_method(A, 1)
        elif not checking_for_different(fun(B), second_derivative(B)):
            print(f"Start from B = {B}, fun(B) = {B} derivative(B) = {derivative(B)}")
            return tangent_method(B, 1)
        else:
            print("Bad fun for this!")
            return 0

    print(f"\n{i}:")
    x = arif_round(x_pred - fun(x_pred) / derivative(x_pred), ROUND_TO_NUM)
    print(f"x = {x}; fun(x) = {fun(x)}; derivative(x) = {derivative(x)}")
    if check(x, fun):
        return x
    else:
        return tangent_method(x, i + 1)


A = 0
B = 3
print("-" * 200)
print("half_division_method")
M = half_division_method(A, B)
print(f"\nans: {M} +-{E} on [{A}:{B}]")
print("-" * 200)

A = -3
B = 0
print("simple_iteration_method")
N = simple_iteration_method(A)
print(f"\nans: {N} +-{E} on [{A}:{B}]")
print("-" * 200)

A = -4
B = N
print("chord_method")
print(f"\nans: {chord_method(A, B)} +-{E} on [{A}:{B}]")
print("-" * 200)

A = N
B = M
print("secant_method")
print(f"\nans: {secant_method(A, B)} +-{E} on [{A}:{B}]")
print("-" * 200)

A = M
B = 4
print("tangent_method")
print(f"\nans: {tangent_method()} +-{E} on [{A}:{B}]")
print("-" * 200)
