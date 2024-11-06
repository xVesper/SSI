import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x / 10) * np.sin(x / 200)

rozrzut = 10
wsp_przyrostu = 1.1
l_iteracji = 100
zakres_zmiennosci = (0, 100)

x = np.random.uniform(zakres_zmiennosci[0], zakres_zmiennosci[1])
y = f(x)

historical_x = [x]
historical_y = [y]
change_points_x = []
change_points_y = []

for iteracja in range(l_iteracji):
    x_pot = x + np.random.uniform(-rozrzut, rozrzut)

    if x_pot < zakres_zmiennosci[0]:
        x_pot = zakres_zmiennosci[0]
    elif x_pot > zakres_zmiennosci[1]:
        x_pot = zakres_zmiennosci[1]

    y_pot = f(x_pot)

    if y_pot >= y:
        x = x_pot
        y = y_pot
        rozrzut *= wsp_przyrostu
        change_points_x.append(x)
        change_points_y.append(y)
    else:
        rozrzut /= wsp_przyrostu
        change_points_x.append(x)
        change_points_y.append(y)

    historical_x.append(x)
    historical_y.append(y)

    if iteracja % 10 == 0:
        print(f"Iteracja: {iteracja}, x: {x:.4f}, y: {y:.4f}, rozrzut: {rozrzut:.4f}")

x_vals = np.linspace(zakres_zmiennosci[0], zakres_zmiennosci[1], 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='Funkcja celu', color='blue')
plt.scatter(historical_x, historical_y, color='red', s=30, label='Pozycje algorytmu')
plt.scatter(change_points_x, change_points_y, color='red', s=60, edgecolors='black', marker='o', label='Punkty zmiany')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Optymalizacja funkcji sin(x/10)*sin(x/200)')
plt.legend()
plt.show()
