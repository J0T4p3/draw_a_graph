
# Leia-me

Este código tem como objetivo calcular a integral definida da função exponencial do seno de x e plota o gráfico da função, juntamente com a visualização da sua área a ser calculada.

## Instalação de bibliotecas e criação do ambiente

Para executar o código, é necessário ter o Python 3 instalado. As seguintes bibliotecas também são necessárias:

- NumPy
- Matplotlib
- SciPy

As bibliotecas podem ser instaladas por meio do pip, executando os seguintes comandos:

```
pip install numpy matplotlib scipy
```

## Explicação do código

O código é dividido em duas funções principais:

1. A função `func(x)`, que retorna o valor de `np.exp(np.sin(x))` para um dado valor de `x`.
2. A função `draw_graph(num_points)`, que plota o gráfico da função, calcula a integral definida da função entre os limites definidos e a área correspondente à integral.

Além disso, há uma função `elapsed_time` usada como decorador para medir o tempo de execução de funções.

O usuário é solicitado a inserir a quantidade de pontos a serem usados no cálculo da integral. A partir daí, o programa gera o gráfico da função com a região acinzentada correspondente à área da integral.

## Execução do código

Para executar o código, abra um terminal na pasta do arquivo `main.py` e execute o seguinte comando:

```
python main.py
```

O programa solicitará ao usuário a quantidade de pontos a serem usados no cálculo da integral. Após inserir a quantidade desejada, o programa exibirá o gráfico da função com a região acinzentada correspondente à área da integral e detalhes como o erro atrelado ao cálculo realizado.
