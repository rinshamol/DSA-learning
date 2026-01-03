
import java.util.Scanner;

public class PerimeterOfCircle{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the radius of the circle:");
        int a = sc.nextInt();
        double p = 2*Math.PI*a;
        System.out.print("Perimeter of circle : " + p);
    }
}