
import java.util.Scanner;

public class AreaOfRhombus{
    public static void main(String[] args) {
        Scanner sc =new  Scanner(System.in);
        System.out.print("Enter two diagonals of rhombus:");
        int d1 = sc.nextInt();
        int d2 = sc.nextInt();
        int area = (d1*d2)/2;
        System.out.print("Area of rhombus:"+ area);
    }
}