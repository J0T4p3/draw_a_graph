import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from time import perf_counter
from scipy.integrate import quad


# Decorator para contar o tempo de execução da função
def elapsed_time(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'Tempo para processar f(x) para todos os pontos: {(end-start)}s')
        return result
    return wrapper


# Função a ser integrada
def func(x):
    return np.exp(np.sin(x))

# Integral definida entre os limites a e b
def integrate(a, b):
    # Função do scipy que calcula a integral definida de f entre a e b e o erro esperado absoluto
    result, error = quad(func, a, b)
    print('Integral: ', result)
    print('Erro absoluto: ', error)
    return result, error

def append_iy(ix):
    iy = []
    # Calcula f(x) para todos os pontos de ix
    for x in ix:
        iy.append(func(x))

    return iy

@elapsed_time
def calculate_total_area(ix, iy):
    total_area = 0
    for i in range(len(ix)-1):
        # Calcula a área de cada retângulo e soma na área total
        total_area += (ix[i+1] - ix[i]) * iy[i]
    return total_area

# Desenha o gráfico da função e região acinzentada como área da integral
def draw_graph(num_points):
    x = np.linspace(-10, 10, num_points)  # Eixo x
    y = func(x)  # Eixo y (calculado pelo numpy)

    # Desenho do gráfico base (em vermelho)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ax.set_ylim(bottom=0)

    # coloca o eixo y no centro do gráfico
    ax.spines['left'].set_position('center')

    ## Região acinzentada do gráfico, calculada usando a quantidade de pontos definida pelo usuário
    # Limites da integral
    a, b = -5, 5
    ix = np.linspace(a, b, num_points) 

    # Função paralelizável.
    iy = append_iy(ix)

    # verts são os vértices necessários para desenhar a área acinzentada
    verts = [(a, 0), *zip(ix, iy), (b, 0)]
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    # Calcula a integral definida entre a e b, retorna o valor da integral e o erro esperados
    r_integer, r_error = integrate(a, b)

    area = calculate_total_area(ix, iy)

    ax.text(0.05, 1.0, 'Integral da função: {0:.5f}\nÁrea do Gráfico: {1:.5f}\nErro estimado: {2:.2e}\nErro real: {3:.4f}\nN de pontos: {4}'.format(r_integer, area,  r_error, abs(r_integer-area), num_points),
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes)

    fig.text(0.9, 0.05, '$x$')
    fig.text(0.5, 0.9, '$y$')

    # remove linhas desnecessárias
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.show()


if __name__=="__main__":
    print('Digite a quantidade de pontos para calcular a integral da função exp(sen(x)):')
    num_points = int(input())
    draw_graph(num_points)

