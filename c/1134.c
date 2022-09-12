#include <stdio.h>

int main (){
	int a, alc=0, gas=0, die=0;
	while (a != 4){
		scanf("%d",&a);
		if (a ==1){
			alc+=1;
		}else if (a == 2 ){
			gas +=1;
		}else if (a ==3){
			die +=1;
		}
	}
	printf("MUITO OBRIGADO\n");
	printf("Alcool: %d\n", alc);
	printf("Gasolina: %d\n", gas);
	printf("Diesel: %d\n", die);
	
	return 0;
}