main(){
    float media,n1,n2,n3,n4;
    printf("Digite 4 notas: \n");
    scanf("%f %f %f %f",&n1,&n2,&n3,&n4);

    while(n1>10 || n2 >10 || n3>10 || n4>10){
        printf("A nota maxima e 10 \n");
        scanf("%f %f %f %f",&n1,&n2,&n3,&n4);
    }

    media = ((n1+n2+n3+n4)/4);
    printf("Media = %2.f \n",media);
    if(media>=7){
        printf("Aprovado \n");
    }else if (media <7 && media >4 ){
        printf("Em analise \n");
    }else{
        printf("Reprovado");
    }
}
