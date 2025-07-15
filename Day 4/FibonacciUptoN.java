
import java.util.Scanner;

public class FibonacciUptoN{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter range of series:");
        int n = sc.nextInt();
        int f = 0;
        int s = 1;
        int i = 0;
        while(i<n+1){
           System.err.print(f + " ");
           int temp = s;
           s = s +f;
           f = temp;
           i++;
        }
    }
}