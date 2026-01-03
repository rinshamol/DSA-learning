
import java.util.Scanner;

public  class PerimeterOfParallelogram{
    public static void main(String[] args) {
        Scanner sc = new  Scanner(System.in);
        System.out.print("Enter base and side of parallelogram:");
        int b = sc.nextInt();
        int s = sc.nextInt();
        int p = 2*(b+s);
        System.out.print("Perimeter of Parallelogram:"+ p);
    }
}