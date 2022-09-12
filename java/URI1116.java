import java.io.IOException;
import java.util.Scanner;
public class URI1116{
 
    public static void main(String[] args) throws IOException {
 
        Scanner ler = new Scanner(System.in);
        int N;
        N = ler.nextInt();

        for(int i=1; i<=N; i++){
            Scanner sc = new Scanner(System.in);
            String linha = sc.nextLine();
            String [] valores = linha.split("\\s");
            int a = Integer.parseInt(valores[0]);
            int b = Integer.parseInt(valores[1]);

            if (b==0){
                System.out.println("divisao impossivel");

            }else{
                System.out.println((double) a/b);
            }
        }
 
    }
 
}