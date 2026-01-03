
import java.util.Scanner;

public class  PerimeterOfEquilateralTriangle{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter one side of the triangle:");
        int s = sc.nextInt();
        int p = 3*s;
        System.out.print("Perimeter of Equilateral triangle:"+p);
    }
}