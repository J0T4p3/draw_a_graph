#include <stdio.h>
#include <mpi.h>

double function(double x) {
    return x * x;  // Função: f(x) = x^2
}

double integral(double a, double b, int n, int rank, int size) {
    double h = (b - a) / n;  // Largura do espaço total dividido pelo n de secções
    double local_sum = 0.0;

    // Controle da quantidade de intervalos para cada nó processar
    int local_n = n / size;
    int local_start = rank * local_n;
    int local_end = local_start + local_n;

    // Ajuste para tratar intervalos que "sobram" na divisão inteira
    if (rank == size - 1) {
        local_end = n;
        local_n = local_end - local_start;
    }

    double start, finish;

    start = MPI_Wtime();
    for (int i = local_start; i < local_end; i++) {
        double x1 = a + i * h;
        double x2 = a + (i + 1) * h;

        double y1 = function(x1);
        double y2 = function(x2);


        double x = (x1 + x2)/2;

        double y = function(x);

        // Utilizando trapezóides
        local_sum += (y1 + y2) * h / 2.0; 

        // Utilizando retângulos
        // local_sum += y * h;
    }
    finish = MPI_Wtime();
    printf("Tempo de execução: %lfs\n\n", finish-start);
    double global_sum = 0.0;
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    return global_sum;
}

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int size, rank;     // Número de processos e o rank do processo atual
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    double a = 0.0;     // Mínimo no eixo x
    double b = 200.0;   // Máximo no eito x
    int n = 9999999;    // Quantidade de intervalos
    

    double result = integral(a, b, n, rank, size);
    

    if (rank == 0) {
        printf("Área entre os pontos %lf e %lf: %f\n", a, b, result);
        
    }

    MPI_Finalize();
    return 0;
}