
import java.util.Scanner;

public  class AreaOfIsoscelesTriangle{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter base and a side of isosceles triangle:");
        int b = sc.nextInt();
        int x = sc.nextInt();
        double area = (b/4.0)* Math.sqrt(4*x*x - b*b);
        System.out.printf("Area of isosceles triangle: %.2f",area);
    }
}