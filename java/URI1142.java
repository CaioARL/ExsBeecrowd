import java.io.IOException;
import java.util.Scanner;
public class URI1142 {
 
    public static void main(String[] args) throws IOException {
 
        int input;
        int x=1;
        int y=2;
        int z=3;
        Scanner ler = new Scanner(System.in);
        input = ler.nextInt();

        for (int a=0; a<input; a++){
            System.out.println(x+" "+y+" "+z+" " +"PUM");
            x+=4;
            y+=4;
            z+=4;
        }
 


    }
 
}