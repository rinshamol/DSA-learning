
import java.util.Scanner;

public  class LowerAndUppercase{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a character:");
        char c = sc.next().trim().charAt(0);
        if(c >= 'A'  &&  c <= 'Z'){
            System.out.println(c +" is Uppercase");
        }else{
            System.out.println(c +" is Lowercase"); 
        }
    }
}