
public class mediaFor {
    public static void main(String[] args) {
    String nome[] = {"Caio", "Pedro", "Leticia", "Bruna" };
    double n1[] = {9,5,5,7,};
    double n2[] = {8,3,6,8};
    double media;

        for(int i=0; i<=3; i++){

            media = (n1[i] + n2[i]) / 2;
            System.out.print(nome[i] + " tirou: " + media + " ");

            if(media >= 6.0){
                System.out.println("{Aprovado}");
            }if(media >= 5.5 && media < 6 ){
                System.out.println("{Avaliando faltas}");
            }if(media < 5.5){ 
                System.out.println("{Reprovado}");
            }

        }
    }
}