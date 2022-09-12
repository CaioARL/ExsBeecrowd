import java.util.Arrays;
public class Array {
    public static void main(String[] args) {
        String[] brics = {"Brasil", "Russia", "India", "China", "África do Sul"};

        for(int i = 0; i < 5; i++){
            System.out.println(brics[i]);
        }

        int position = Arrays.binarySearch(brics, "Brasil");
        System.out.println("Brasil está na posição = " + position);

    }
}