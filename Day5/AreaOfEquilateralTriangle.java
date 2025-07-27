
import java.util.Scanner;

public class AreaOfEquilateralTriangle{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the side of the triangle:");
        int s = sc.nextInt();
        double area = (Math.sqrt(3)/4)*s*s;
        System.out.printf("Area of an equilateral triangle: %.2f",area);
    }
}