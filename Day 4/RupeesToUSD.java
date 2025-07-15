
import java.util.Scanner;

public class RupeesToUSD{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter currency in rupees:");
        int rs = sc.nextInt();
        float USD;
        USD = rs/83.50f;
        System.out.print("USD:" + USD);
    }
}