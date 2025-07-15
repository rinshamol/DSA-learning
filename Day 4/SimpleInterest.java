import java.util.Scanner;
public class SimpleInterest{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter principle amount, rate of Interest, and Time in years:");
        int p = sc.nextInt();
        float i = sc.nextFloat();
        float r = i/100;
        float t = sc.nextFloat();
        float si = p*r*t;
        System.out.println("Simple interest : " + si);
    }
}