import matplotlib.pyplot as plt


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
