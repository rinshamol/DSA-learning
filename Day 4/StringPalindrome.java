
import java.util.Scanner;

public class StringPalindrome{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a word:");
        String str = sc.next();
        StringBuilder rev = new StringBuilder(str);                         //stringBuilder creates multiple objects of series of characters
        String reverse = rev.reverse().toString();
        if(str.equals(reverse)){
            System.out.println("Pallindrome");
        }else{
            System.out.println("Not Pallindrome");
        }
    }
}