
import java.util.Scanner;

public  class CountOfDigit{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number:");
        int n = sc.nextInt();
        int b = n;
        System.err.print("Enter a digit to find its occurance:");
        int a = sc.nextInt();
        int count = 0;
        while( n > 0 ){
            int r = n % 10;
            if( a == r){
                count++;
            }
            n = n/10;
        } 
        System.out.print("Count of " + a + " in " + b + " : " + count);
    }
}