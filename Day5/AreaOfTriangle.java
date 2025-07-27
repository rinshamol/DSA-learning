
import java.util.Scanner;

public class AreaOfTriangle{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length of three sides of triangle:");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        double s ;
        s = (double)(a+b+c)/2;
        double d = s*(s-a)*(s-b)*(s-c);
        double area = Math.sqrt(d);
        System.out.println("Area of triangle with three sides :" + area);

    }
}