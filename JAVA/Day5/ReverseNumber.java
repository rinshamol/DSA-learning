
import java.util.Scanner;

public  class  ReverseNumber{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number:");
        int a = sc.nextInt();
        int n = a;
        int rev = 0;
        while( n > 0 ){
            int r = n % 10;
            rev = rev*10 + r;
            n = n/10;
        }
        System.out.print("Reverse of "+ a +" : " + rev);
    }
}