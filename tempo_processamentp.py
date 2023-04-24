import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from time import perf_counter


def func(x):
    return x ** 2 + x ** 3 + 500

def draw_graph(num_points):
    a, b = 2, 9  # Limites da integral
    x = np.linspace(0, 10) # Eixo x
    y = func(x) # Eixo y (cálculado pelo numpy)

    # Desenho do gráfico base (em vermelho)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ax.set_ylim(bottom=0)

    # Região acinzentada do gráfico, calculada usando a quantidade de pontos definida pelo usuário
    verts = [(a,0), (b,0)]
    
    ix = np.linspace(a, b, num_points)
    
    start = perf_counter()
    iy = func(ix)
    end = perf_counter()
    print(f'Elapsed time to process f(x) for all points: {end-start}')

    verts = [(b, 0), (a, 0), *zip(ix, iy)] # This is capable to be parallelized
    start = perf_counter()
    # poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    # ax.add_patch(poly)
    # end = perf_counter()
    # print(f'Elapsed time to plot the points: {end-start}')

    fig.text(0.9, 0.05, '$x$')
    fig.text(0.1, 0.9, '$y$')

    ax.spines[['top', 'right']].set_visible(False)
    # ax.set_xticks([a, b], labels=['$a$', '$b$'])

    plt.show()
    
    
draw_graph(1000000000)