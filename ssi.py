import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import pi
import numpy as np
import random

from pandas.errors import EmptyDataError


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

print(data_load())

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

#draw_smile()

def list_classes(df):
    classes_col = df['class']
    classes=[]
    for x in classes_col:
        if x not in classes:
            classes.append(x)
        return classes

#pierwsza seria

x1 = data_load()['petal_length_in_cm']
y1 = data_load()['petal_width_in_cm']
classes = data_load()['class']

unique_classes  = np.unique(classes)
names = ['Setosa', 'Versicolor', 'Virginica']

colors = ['red', 'blue', 'green']

for i, clas in enumerate(unique_classes):
    plt.scatter(x1[classes == clas], y1[classes == clas], label=names[i], color=colors[i])

plt.xlabel('petal_length_in_cm')
plt.ylabel('petal_width_in_cm')
plt.legend()
#plt.show()