import java.io.IOException;
import java.util.Scanner;

public class URI1114 {
	
	public static void main(String[] args) throws IOException {
		try (Scanner leitor = new Scanner(System.in)) {
			int n;
			n = leitor.nextInt();

			while (n != 2002){
                System.out.println("Senha Invalida");
				n = leitor.nextInt();
            }
			if (n == 2002){
				System.out.println("Acesso Permitido");
			}
		}
	}
	
}