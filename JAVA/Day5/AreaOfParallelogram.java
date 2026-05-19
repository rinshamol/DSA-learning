
import java.util.Scanner;

public class AreaOfParallelogram{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter  base and height of parallelogram:");
        int b = sc.nextInt();
        int h = sc.nextInt();
        int area = b*h;
        System.out.print("Area of a parallelogram:"+area);
    }
}