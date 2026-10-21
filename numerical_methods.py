"""
Практическая работа №2: Численные методы решения уравнений.
Демонстрирует применение Matplotlib, NumPy и алгоритмов (дихотомия, Ньютон).
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    """Исходная функция: e^(-1.08x) + x^2 - 2"""
    return np.exp(-1.08 * x) + x**2 - 2

# --- 1. Графический метод (поиск корней) ---
x_vals = np.linspace(-2, 2.5, 1000)
y_vals = f(x_vals)

plt.figure(figsize=(10, 5))
plt.plot(x_vals, y_vals, label='f(x) = e^(-1.08x) + x^2 - 2', color='blue')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title("Графический метод локализации корней")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()

# --- 2. Метод дихотомии (бисекции) ---
def dihotomia(x1, x2, eps=1e-6):
    ksi = (x1 + x2) / 2
    while abs(f(ksi)) > eps:
        if (f(x1) > 0 and f(ksi) < 0) or (f(x1) < 0 and f(ksi) > 0):
            x2 = ksi
        elif (f(ksi) > 0 and f(x2) < 0) or (f(ksi) < 0 and f(x2) > 0):
            x1 = ksi
        ksi = (x1 + x2) / 2
    return ksi

root_dihot = dihotomia(1.0, 2.0)
print(f"Метод дихотомии (корень 1): x = {root_dihot:.6f}")

# --- 3. Метод Ньютона ---
def f_prime(x):
    """Производная f(x)"""
    return -1.08 * np.exp(-1.08 * x) + 2 * x

def newton(a, b, eps=1e-5):
    xn = (a + b) / 2
    xn1 = xn - f(xn) / f_prime(xn)
    while abs(xn1 - xn) > eps:
        xn = xn1
        xn1 = xn - f(xn) / f_prime(xn)
    return xn1

root_newton = newton(1.0, 2.0)
print(f"Метод Ньютона (корень 1): x = {root_newton:.6f}")

# --- 4. Метод простой итерации ---
def iterat(a, b, eps=1e-5):
    xn = (a + b) / 2
    # Итерационная функция: x = x - f(x)/5 (коэффициент подобран для сходимости)
    xn1 = abs(xn - f(xn) / 5) 
    while abs(xn1 - xn) > eps:
        xn = xn1
        xn1 = abs(xn - f(xn) / 5)
    return xn1

root_iter = iterat(1.0, 2.0)
print(f"Метод итерации (корень 1): x = {root_iter:.6f}")
