#include <stdio.h>
 
int main() {
 int n, soma=0;
 double media, div=0;
    while (1)
    {
        scanf("%d",&n);
        if (n<0)
            break;       
        else{
            soma+=n;
            div++;
        }
    }

    media = soma / div;
    printf("%.2lf\n",media);
 
    return 0;
}