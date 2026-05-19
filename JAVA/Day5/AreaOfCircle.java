
import java.util.Scanner;

public class AreaOfCircle{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Radius of the circle:");
        int r = sc.nextInt();
        double area = Math.PI*r*r;
        System.out.printf("Area of circle : %.2f", area);
    }
}