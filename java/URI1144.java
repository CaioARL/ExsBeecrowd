import java.io.IOException;
import java.util.Scanner;
public class URI1144 {
 
    public static void main(String[] args) throws IOException {
    int n;
    Scanner ler = new Scanner(System.in);
    n = ler.nextInt();

    while(n<1 || n>1000){
        n = ler.nextInt();
    }

    for(int i =1; i<=n; i++){
        System.out.println(i+" "+(i*i)+" "+(i*i*i));
        System.out.println(i+" "+((i*i)+1)+" "+(i*i*i+1));
    }
        
    }
 
}