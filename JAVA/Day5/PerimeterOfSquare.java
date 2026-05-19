
import java.util.Scanner;

class PerimeterOfSquare{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter one side of Square:");
        int s = sc.nextInt();
        int p = 4*s;
        System.out.print("Perimeter of Square:"+ p);
        
    }
}