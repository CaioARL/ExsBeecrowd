#include<stdio.h>
#include<stdlib.h>

float calculoVantagens(float *numeroHoras, float *salarioHora, int *numeroFilhos, float *valorPorFilho);
float calculoDeducoes(float *salarioBruto, float *taxaIR);

int main()
{
    int numeroFilhos;
    float numeroHoras, salarioHora, valorPorFilho, taxaIR, salarioBruto, salarioFamilia, vantagens, INSS, IRPF, deducoes;

    printf("Digite o numero de horas:\n");
    scanf("%f", &numeroHoras);

    printf("Digite o salario/hora:\n");
    scanf("%f", &salarioHora);

    printf("Digite o numero de filhos:\n");
    scanf("%d", &numeroFilhos);

    printf("Digite o valor por filho:\n");
    scanf("%f", &valorPorFilho);

    printf("Digite a taxa IR:\n");
    scanf("%f", &taxaIR);

    salarioBruto = (calculoVantagens(&numeroHoras, &salarioHora, &numeroFilhos, &valorPorFilho));

    calculoDeducoes(&salarioBruto, &taxaIR);

    return 0;
}

float calculoVantagens(float *numeroHoras, float *salarioHora, int *numeroFilhos, float *valorPorFilho)
{
    float salarioBruto, salarioFamilia, vantagens;

    salarioBruto = *numeroHoras * *salarioHora;
    salarioFamilia = *numeroFilhos * *valorPorFilho;
    vantagens = salarioBruto + salarioFamilia;

    printf("Salario Bruto: %.2f\n", salarioBruto);
    printf("Salario Familia: %.2f\n", salarioFamilia);
    printf("Vantagens: %.2f\n", vantagens);

    return (salarioBruto);

}

float calculoDeducoes(float *salarioBruto, float *taxaIR)
{
    float INSS, IRPF, deducoes;

    INSS = (*salarioBruto * 8) / 100;
    IRPF = *salarioBruto * *taxaIR;
    deducoes = INSS + IRPF;

    printf("INSS: %.2f\n", INSS);
    printf("IRPF: %.2f\n", IRPF);
    printf("Deducoes: %.2f\n", deducoes);

}