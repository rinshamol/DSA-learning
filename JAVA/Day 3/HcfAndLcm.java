
import java.util.Scanner;

public class HcfAndLcm {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Two numbers:");
        int a  = sc.nextInt();
        int b = sc.nextInt();
        int x = a ;
        int y = b;
        int c ;
        int hcf = 0;
        int lcm;
        while(b != 0){
            c = a % b;
            a = b;
            hcf = b;
            b = c;
        }
        System.out.println("hcf:"+ hcf);
        lcm = (x * y) / hcf;
        System.out.println("lcm:"+ lcm);
    }
}