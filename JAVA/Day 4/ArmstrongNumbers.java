
import java.util.Scanner;

public class ArmstrongNumbers{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter start and end ranges:");
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.print("Armstrong numbers are:");
        for(int i=a; i<= b; i++){
            int n = i;
            int nLen = lengthInt(n);
            int sum = 0;
            while(n!=0){
                int r = n%10;
                int pow =(int)Math.pow(r, nLen);
                sum = sum + pow;
                n = n/10;
            }
            if(sum == i){
                System.out.print(i + " ");
            }
        }
    }
    public static  int lengthInt(int n){
        if (n == 0) return  1;
        int count = 0;
        while(n!=0){
          n = n/10;
          count++;  
        }
        return  count;
    }
}