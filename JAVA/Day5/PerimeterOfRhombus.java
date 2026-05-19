
import java.util.Scanner;

class PerimeterOfRhombus{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter one side of Rhombus:");
        int s = sc.nextInt();
        int p = 4*s;
        System.out.print("Perimeter of Rhombus:"+ p);
    }
}