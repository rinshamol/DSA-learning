public class SubstractSumAndProduct {
    public static void main(String[] args) {
        int a = 4421;
        int prod = 1;
        int sum = 0;
        while(a > 0) {
            int r = a % 10;
            prod *= r;
            sum += r;
            a = a/10;
        }
        System.out.println(prod - sum);
    }
}
