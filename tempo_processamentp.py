import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from time import perf_counter
from scipy.integrate import quad


# decorator para contar o tempo de execução da função
def elapsed_time(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'Tempo para proessar f(x) para todos os pontos: {end-start}')
        return result
    return wrapper


# Integral definida entre os limites a e b
def integrate(f, a, b):
    # Função do scipy que calcula a integral definida de f entre a e b
    result, error = quad(f, a, b)
    print('Integral value: ', result)
    print('Error: ', error)
    return result


# Função a ser integrada
@elapsed_time
def func(x):
    return np.sin(np.pi * x) + np.cos(2 * np.pi * x)


# Desenha o gráfico da função e a região acinzentada
def draw_graph(num_points):
    a, b = -5, 5  # Limites da integral
    x = np.linspace(-10, 10)  # Eixo x
    y = func(x)  # Eixo y (cálculado pelo numpy)

    # Desenho do gráfico base (em vermelho)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)

    # Região acinzentada do gráfico, calculada usando a quantidade de pontos definida pelo usuário
    ix = np.linspace(a, b, num_points)
    iy = func(ix)
    # verts são os vértices necessários para desenhar a área acinzentada
    verts = [(b, 0), (a, 0), *zip(ix, iy)]
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    fig.text(0.9, 0.05, '$x$')
    fig.text(0.1, 0.9, '$y$')

    ax.spines[['top', 'right']].set_visible(False)
    # ax.set_xticks([a, b], labels=['$a$', '$b$'])

    plt.show()


draw_graph(1000000)
