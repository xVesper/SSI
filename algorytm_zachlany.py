import math
import matplotlib.pyplot as plt

def manhattan_odleglosc(punktA, punktB):
    return abs(punktA[0] - punktB[0]) + abs(punktA[1] - punktB[1])

def miara_niepodobienstwa(bitmapaA, bitmapaB):
    miara = 0
    wysokosc, szerokosc = len(bitmapaA), len(bitmapaA[0])

    czarne_punkty_A = [(i, j) for i in range(wysokosc) for j in range(szerokosc) if bitmapaA[i][j] == 1]
    czarne_punkty_B = [(i, j) for i in range(wysokosc) for j in range(szerokosc) if bitmapaB[i][j] == 1]

    for punktA in czarne_punkty_A:
        odl_min = float('inf')
        for punktB in czarne_punkty_B:
            odl_akt = manhattan_odleglosc(punktA, punktB)  # Zmieniamy na odległość Manhattan
            odl_min = min(odl_min, odl_akt)
        miara += odl_min

    return miara

def miara_podobienstwa_obustronnego(bitmapaA, bitmapaB):
    miara_A_B = miara_niepodobienstwa(bitmapaA, bitmapaB)
    miara_B_A = miara_niepodobienstwa(bitmapaB, bitmapaA)

    return -(miara_A_B + miara_B_A)

def znajdz_najbardziej_podobna_bitmape(bitmapa_testowa, bitmapy_wzorcowe):
    najlepsza_miara = float('-inf')
    najlepsza_bmp = None

    for i, bitmapa_wzorcowa in enumerate(bitmapy_wzorcowe):
        miara = miara_podobienstwa_obustronnego(bitmapa_testowa, bitmapa_wzorcowa)
        print(f"Miara podobieństwa dla wzorca {i + 1}: {miara}")

        if miara > najlepsza_miara:
            najlepsza_miara = miara
            najlepsza_bmp = i + 1

    return najlepsza_bmp

def rysuj_bitmapy(bitmapa_testowa, bitmapy_wzorcowe, najlepsza_bmp):
    fig, axes = plt.subplots(1, len(bitmapy_wzorcowe) + 1, figsize=(12, 4))

    axes[0].imshow(bitmapa_testowa, cmap='gray', interpolation='nearest')
    axes[0].set_title('Bitmapa Testowa')
    axes[0].axis('off')

    for i, bitmapa_wzorcowa in enumerate(bitmapy_wzorcowe):
        axes[i + 1].imshow(bitmapa_wzorcowa, cmap='gray', interpolation='nearest')
        axes[i + 1].set_title(f'Wzorzec {i + 1}')
        axes[i + 1].axis('off')
        if i + 1 == najlepsza_bmp:
            axes[i + 1].set_facecolor('yellow')

    plt.tight_layout()
    plt.show()

bitmapa_testowa1 = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
]

bitmapa_wzorcowa1 = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]

bitmapa_wzorcowa2 = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

bitmapa_wzorcowa3 = [
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0]
]

bitmapy_wzorcowe = [bitmapa_wzorcowa1, bitmapa_wzorcowa2, bitmapa_wzorcowa3]

najbardziej_podobna = znajdz_najbardziej_podobna_bitmape(bitmapa_testowa1, bitmapy_wzorcowe)

rysuj_bitmapy(bitmapa_testowa1, bitmapy_wzorcowe, najbardziej_podobna)
