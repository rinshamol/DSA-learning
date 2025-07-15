import java.util.Scanner;
public class OddOrEven{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number:");
        int num = sc.nextInt();
        int a = num;
        if(num % 2 == 0){
            System.err.println(a +" is even number");
        }else{
            System.err.println(a + " is odd number");
        }
    }
}