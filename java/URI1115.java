import java.io.IOException;
import java.util.Scanner;
public class URI1115 {
 
    public static void main(String[] args) throws IOException {

        Scanner ler = new Scanner(System.in);
        int x,y;
        x = ler.nextInt();
        y = ler.nextInt();
        
        while((x!=0) || (y!=0)){
            
            if ((x>0) && (y>0)){
                System.out.println("primeiro");
                x = ler.nextInt();
                y = ler.nextInt();
            }
            if ((x<0) && (y>0)){
                System.out.println("segundo");
                x = ler.nextInt();
                y = ler.nextInt();
            }
            if ((x<0) && (y<0)){
                System.out.println("terceiro");
                x = ler.nextInt();
                y = ler.nextInt();
            }
            if ((x>0) && (y<0)){
                System.out.println("quarto");
                x = ler.nextInt();
                y = ler.nextInt();
            }
        }

    }
 
}