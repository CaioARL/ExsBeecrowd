import java.util.Scanner;
public class Ex1001 {
    
    public static void main (String[] args){
        int A,B,soma;
        try (Scanner ler = new Scanner(System.in)) {
            A = ler.nextInt();
            B = ler.nextInt();
        }
        soma = A + B;
        System.out.println("X = " +soma );
    }
}
