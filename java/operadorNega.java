public class operadorNega {
    public static void main(String[] args) {
        boolean a = true;
        boolean b = false;
        boolean c = true;
        System.out.println(!a);
        System.out.println(!b);
        System.out.println(!(a && b));
        System.out.println(!(a && c));
        System.out.println(!(a || b));
        System.out.println(!(a || c));
    }
}
