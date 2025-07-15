import java.util.Scanner;
public class Calculate{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two numbers and an operator(+, -, /, *, %)");
        int a = sc.nextInt();
        int b = sc.nextInt();
        char c = sc.next().charAt(0);
        float res = 0;
        String operation = "Error";
        if(c == '+'){
            res = a + b;
            operation = "Sum";
        }
         if(c == '-'){
            res = a -b;
            operation = "difference";
        }
         if(c == '/'){
            res = a/b;
            operation = "division";
        }
         if(c == '*'){
            res = a*b;
            operation = "product";
         }
         if(c == '%'){
            res = a%b;
            operation = "reminder after division";
         }
         System.out.println(operation+ " : " + res);
    }
}