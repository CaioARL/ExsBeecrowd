import java.io.IOException;
import java.util.Scanner;
public class URI1117     {
    
 
    public static void main(String[] args) throws IOException {

        int i = 0;
        float a = 0;
        float media = 0;
        Scanner ler = new Scanner(System.in);

        while (i<2){
            a = ler.nextFloat();
            if((a>0) && (a<=10)){
                media+=a;
                i+=1;
            }
            else{
                System.out.println("nota invalida\n");
            }
        }
        media = media/2;
        System.out.printf("media = %.2f\n", media);

    }
 
}