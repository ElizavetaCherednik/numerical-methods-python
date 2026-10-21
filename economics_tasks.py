"""
Практическая работа №1: Экономические и вычислительные задачи.
Демонстрирует работу с функциями, lambda, декораторами и NumPy.
"""
import numpy as np
import math

# --- Задание 1: Функции выручки, издержек и прибыли ---
def revenue(Q, p=70):
    return p * Q

def cost(Q, a=33, b=850):
    return a * Q + b

def profit(Q):
    return revenue(Q) - cost(Q)

print("--- Задание 1 ---")
print(f"Прибыль при Q=190: {profit(190)} руб.")

# --- Задание 2: Lambda-выражение для скидки ---
print("\n--- Задание 2 ---")
final_price = lambda p, d: p * (1 - d / 100)
print(f"Цена со скидкой: {final_price(250, 23)} руб.")

# --- Задание 3: Аналог map ---
print("\n--- Задание 3 ---")
def apply_to_all(f, values):
    return [f(x) for x in values]

cost_func = lambda x: 6.4 * x**2
values = [10, 17, 33, 54, 55]
print(f"Затраты: {apply_to_all(cost_func, values)}")

# --- Задание 4: Декоратор ---
print("\n--- Задание 4 ---")
calls = 0
def count_calls(func):
    def wrapper(Q):
        global calls
        calls += 1
        result = func(Q)
        print(f"Вызов {calls}: Q={Q}, Прибыль={result}")
        return result
    return wrapper

profit_decorated = count_calls(profit)
profit_decorated(180)
profit_decorated(190)
profit_decorated(200)

# --- Задание 5: Квадратичная функция и безубыточность ---
print("\n--- Задание 5 ---")
def profit_quad(Q): return -1 * Q**2 + 170 * Q - 3625
a, b, c = -1, 170, -3625
D = b**2 - 4 * a * c
print(f"Дискриминант: {D}")
if D > 0:
    Q1 = (-b + math.sqrt(D)) / (2 * a)
    Q2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"Точки безубыточности: Q1={Q1}, Q2={Q2}")
Q_star = -b / (2 * a)
print(f"Максимум прибыли: Q*={Q_star}, Profit={profit_quad(Q_star)}")

# --- Задание 6: Векторизация классификации ---
print("\n--- Задание 6 ---")
def classify_result(x):
    if x > 0: return 1
    elif x < 0: return -1
    return 0

results = [-1500, -150, 0, -500, 250, 1250, 1400]
arr = np.array(results)
classify = np.vectorize(classify_result)
print(f"Классификация: {classify(arr)}")

# --- Задание 7: Срезы массивов ---
print("\n--- Задание 7 ---")
prices = np.array([995, 435, 900, 970, 860, 995, 570, 465, 205])
print(f"Первый и последний: {prices[0]}, {prices[-1]}")
print(f"С 2 по 5: {prices[1:5]}")
print(f"В обратном порядке: {prices[::-1]}")
print(f"Каждый второй: {prices[::2]}")

# --- Задание 8: Булева индексация ---
print("\n--- Задание 8 ---")
returns = np.array([-6.3, -10.0, 12.9, -4.0, 0.5, -8.3, 6.5, 5.7, 8.1])
print(f"Положительные: {returns[returns > 0]}")
print(f"Ниже -4.0: {(returns < -4.0).sum()} дней")
filtered_returns = returns.copy()
filtered_returns[filtered_returns < -4.0] = 0
print(f"Обнуленные: {filtered_returns}")

# --- Задание 9: Матрицы и Broadcasting ---
print("\n--- Задание 9 ---")
sales = np.array([[70, 195, 190, 55], [260, 165, 270, 10], [170, 220, 195, 115]])
print(f"Сумма по товарам: {sales.sum(axis=1)}")
print(f"Сумма по месяцам: {sales.sum(axis=0)}")
mean_month = sales.mean(axis=0)
print(f"Средние по месяцам: {mean_month}")
print(f"Отклонения (Broadcasting):\n{sales - mean_month}")

# --- Задание 10: Модель Леонтьева ---
print("\n--- Задание 10 ---")
A = np.array([[0.72, 0.2, 0.4], [0.39, 0.88, 0.22], [0.11, 0.3, 0.85]])
b = np.array([120, 110, 90])
E = np.eye(3)
x = np.linalg.solve(E - A, b)
print(f"Вектор валового выпуска: {x}")
print(f"Проверка решения: {np.allclose((E - A) @ x, b)}")
