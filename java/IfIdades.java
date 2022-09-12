public class IfIdades {
    public static void main(String[] args) {
        int idade = 41;
        if(idade <= 10){
            System.out.println("criança");
        }else if(idade > 10 && idade < 18){
            System.out.println("Joven");
        } else if(idade > 18 && idade < 40){
            System.out.println("Adulto");
        }else{
            System.out.println("Velhaco");
        }
    }
}
