import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

def data_load():
    try:
        df = pd.read_csv('iris.txt', delimiter=r"\s+")
    except FileNotFoundError:
        raise FileNotFoundError("Plik 'iris.txt' nie został znaleziony.")
    except pd.errors.ParserError:
        raise ValueError("Wystąpił problem z formatowaniem pliku 'iris.txt'. Sprawdź poprawność danych.")

    try:
        df2 = pd.read_csv('iris-type.txt', header=None, delimiter=r"\s+")
    except FileNotFoundError:
        raise FileNotFoundError("Plik 'iris-type.txt' nie został znaleziony.")
    except pd.errors.ParserError:
        raise ValueError("Wystąpił problem z formatowaniem pliku 'iris-type.txt'. Sprawdź poprawność danych.")

    column_names = df2[0].tolist()
    column_names[-1] = 'class'
    df.columns = column_names

    return df

# data_load()

def draw_smile():

    fig, ax = plt.subplots()
    circle = Circle((0, 0), radius=2, edgecolor='red', facecolor='white', label='Okrąg')
    ax.add_patch(circle)
    x_smile = np.linspace(-1, 1, 100)
    y_smile = -1 + 1 * (x_smile**2)
    ax.plot(x_smile, y_smile, color='yellow', label='Sinus')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.plot(-1, 1, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="blue", label='Punkty')
    ax.plot(0, 0, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="blue", )
    ax.plot(1, 1, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="blue", )
    plt.grid(True)
    pos = ax.get_position()
    ax.set_position([pos.x0, pos.y0, pos.width * 1.5, pos.height])
    ax.legend(loc='center right', bbox_to_anchor=(1.5, 0.5))
    plt.show()

# draw_smile()

def list_classes(df):
    classes_col = df['class']
    classes=[]
    for x in classes_col:
        if x not in classes:
            classes.append(x)
        return classes

x1 = data_load()['petal_length_in_cm']
y1 = data_load()['petal_width_in_cm']
x2 = data_load()['sepal_width_in_cm']
y2 = data_load()['petal_width_in_cm']
x3 = data_load()['sepal_length_in_cm']
y3 = data_load()['petal_width_in_cm']
x4 = data_load()['sepal_width_in_cm']
y4 = data_load()['petal_length_in_cm']
classes = data_load()['class']

unique_classes  = np.unique(classes)
names = ['Setosa', 'Versicolor', 'Virginica']

colors = ['red', 'blue', 'green']

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

for i, clas in enumerate(unique_classes):
    axs[0, 0].scatter(x1[classes == clas], y1[classes == clas], label=names[i], color=colors[i])
    axs[0, 0].set_xlabel('petal_length_in_cm')
    axs[0, 0].set_ylabel('petal_width_in_cm')
    axs[0, 0].legend()
    axs[0, 1].scatter(x2[classes == clas], y2[classes == clas], label=names[i], color=colors[i])
    axs[0, 1].set_xlabel('petal_length_in_cm')
    axs[0, 1].set_ylabel('petal_width_in_cm')
    axs[0, 1].legend()
    axs[1, 0].scatter(x3[classes == clas], y3[classes == clas], label=names[i], color=colors[i])
    axs[1, 0].set_xlabel('petal_length_in_cm')
    axs[1, 0].set_ylabel('petal_width_in_cm')
    axs[1, 0].legend()
    axs[1, 1].scatter(x4[classes == clas], y4[classes == clas], label=names[i], color=colors[i])
    axs[1, 1].set_xlabel('petal_width_in_cm')
    axs[1, 1].set_ylabel('petal_length_in_cm')
    axs[1, 1].legend()

# plt.show()

def k_sre():

    data = np.loadtxt('spirala.txt')
    n = 4
    iter = 100

    middle = data[np.random.choice(data.shape[0], n, replace=False)]

    for _ in range(iter):
        distances = np.zeros((data.shape[0], n))

        for i in range(data.shape[0]):
            for k in range(n):
                distances[i, k] = np.sqrt(np.sum((data[i] - middle[k]) ** 2))
        labels = np.argmin(distances, axis=1)

        new_middle = np.array([data[labels == i].mean(axis=0) for i in range(n)])
        if np.all(middle == new_middle):
            break

        middle = new_middle

    plt.figure(figsize=(8, 6))
    for i in range(n):
        plt.scatter(data[labels == i][:, 0], data[labels == i][:, 1], s=20, alpha=.70, label=f'Klaster {i + 1}')
    plt.scatter(new_middle[:, 0], new_middle[:, 1], color='red', s=100, marker='x', label='Środki', linewidths=2)
    plt.title("K-Średnich")
    plt.legend()
    plt.show()

#k_sre()

def algorithm():

    zakres_zmiennosci = [0, 100]

    x_plot = np.linspace(zakres_zmiennosci[0], zakres_zmiennosci[1], 1000)
    y_plot = np.sin(x_plot/10)*np.sin(x_plot/200)

    x = np.random.uniform(zakres_zmiennosci[0], zakres_zmiennosci[1])
    y = np.sin(x / 10) * np.sin(x / 200)

    rozrzut = 10
    wsp_przyrostu = 1.1
    iteracja = 100

    for _ in range(iteracja):
        x_pot = x + np.random.uniform(-rozrzut, rozrzut)

        if x_pot > zakres_zmiennosci[1]:
            x_pot = zakres_zmiennosci[1]
        elif x_pot < zakres_zmiennosci[0]:
            x_pot = zakres_zmiennosci[0]

        y_pot = np.sin(x_pot / 10) * np.sin(x_pot / 200)

        if y_pot >= y:
            x = x_pot
            y = y_pot
            rozrzut *= wsp_przyrostu
        else:
            rozrzut /= wsp_przyrostu
        plt.scatter(x, y, color='k', label=f'({x:.2f}, {y:.2f})')
        print('nr iteracji: ', _, ": ", x,y, rozrzut)

    plt.plot(x_plot, y_plot, linestyle='-', color='k', label='Funkcja')
    plt.scatter(x, y, color='r', label=f'({x:.2f}, {y:.2f})', marker=".", linewidths=5)
    plt.title("Algorytm 1 + 1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

#algorithm()
