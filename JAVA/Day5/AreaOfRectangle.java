
import java.util.Scanner;

public class AreaOfRectangle{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two sides of a rectangle:");
        int a = sc.nextInt();
        int b = sc. nextInt();
        int area = a*b;
        System.out.print("Area of Rectangle:"+ area);
    }
}