import java.util.Scanner;

public class PrimeNumber{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number:");
        int n = sc.nextInt();
        int b = 2;
        boolean flag = false;
        while( b < n/2 ){
            if(n % b == 0){
                flag = true;
            }
            b++;
        }
        if(flag == true){
            System.out.println("The number "+ n + " is not a prime number");
        }else{
            System.out.println("The number "+ n + " is a prime number");
        }
    }
}