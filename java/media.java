
class Media{
    double nota1;
    double nota2;
    double media;
    String n;

    public Media(double nota1, double nota2){
        this.media = (nota1 + nota2)/2;
        
        if(media >= 6){
            n= "Aprovado";
        }else{
            n="Reprovado";
        }

    }
    public static void main(String[] args) {
        Media med1 = new Media(5.5, 5.5);
        Media med2 = new Media(7.0, 6.5);
        Media med3 = new Media(6.0, 8.0);
        Media med4 = new Media(4.5, 5.5);
        System.out.print("Media = " + med1.media+ " ");
        System.out.println("Situacao = " + med2.n);
        System.out.print("Media = " + med2.media+ " ");
        System.out.println("Situacao = " + med3.n);
        System.out.print("Media = " + med3.media+ " ");
        System.out.println("Situacao = " + med3.n);
        System.out.print("Media = " + med4.media+ " ");
        System.out.println("Situacao = " + med4.n);
    }

}