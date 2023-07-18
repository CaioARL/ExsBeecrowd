import java.util.Scanner;

public class URI1183 {

	public static void main(String[] args) {
		
		Double[][] m = new Double[12][12];
		
		Scanner leitor = new Scanner(System.in);
		String op = leitor.next().toUpperCase();
		
		for (int i = 0; i < m.length; i++) {
			for (int j = 0; j < m.length; j++) { 
				m[i][j] = leitor.nextDouble();
			}
		}
		 double res = realizaCalc(m);
		 
		 if (op.equals("S")) {
			 System.out.printf("%.1f\n", res);
		 }else {
			 System.out.printf("%.1f\n", res/66);
		 }
	}
	
	public static double realizaCalc(Double[][] matriz) {
		double soma = 0;
		
		for (int i = 0; i < matriz.length+1; i++) {
			for (int j = i+1; j < matriz.length; j++) {
				soma += matriz[i][j]; 
			}
		}
		
		return soma;
		
	}
	
}
