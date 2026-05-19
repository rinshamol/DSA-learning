
import java.util.Scanner;

public class PerimeterOfRectangle{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length and width of Rectangle:");
        int l = sc.nextInt();
        int w = sc.nextInt();
        int p = 2*(l+w);
        System.out.print("Perimeter of Rectangle:"+ p);
        
    }
} 