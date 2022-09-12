#include <stdio.h>
#include <locale.h>
int main()
{
    setlocale(LC_ALL, "Portuguese");
    int n, i, j, num = 1;
    printf("Digite o número de linhas:\n ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= i; ++j)
        {
            printf("%d ", num);
            ++num;
        }
        printf("\n");
    }
    return 0;
}