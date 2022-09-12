import java.io.IOException;
import java.util.Scanner;

public class URI1153 {

    public static void main(String[] args) throws IOException {

        int n;
        int fatorial=1;
        Scanner ler = new Scanner(System.in);
        n = ler.nextInt();

        while(n>13 || n <0){
            n = ler.nextInt();
        }

        for (int i=1; i<=n; i++) {
            fatorial *= i;
        }
        System.out.println(fatorial);
    }

}