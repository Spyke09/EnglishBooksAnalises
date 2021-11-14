from program import analise
import matplotlib.pyplot as plt
from src.utils import get_root


def circle_plot(d: dict):
    d = delete_zeros(d)
    keys, values = d.keys(), d.values()
    fig, ax = plt.subplots()
    ax.pie(values, labels=keys)
    return fig


def delete_zeros(d: dict):
    nd = dict()
    for i, j in d.items():
        if j > 0:
            nd[i] = j
    return nd


def get_lines(n, translate_n):
    for i, j, k in analise.get_difficult_data(n, translate_n):
        yield f"{round(i*100, 2)}%".ljust(7) + f"{j}: {', '.join(k)}"

