public class ArraysDuo {
    public static void main(String[] args) {
        String[] [] aluno = {{"Caio", "masc", "ADS"}, {"João", "masc" ,"TCC" }};

        for(int x=0; x <2; x++){
            for(int y=0; y<3; y++){
                System.out.println(aluno[x][y]);
            }
        }
    }
}
