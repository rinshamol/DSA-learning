import java.util.Scanner;
public  class StarPrint{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Start Entering numbers ......");
        int sum = 0;
        String n;
        while(true){
            n = sc.next();
            if(n.equals("*")) break;
            sum = sum + Integer.parseInt(n); 
        }
        System.out.println("Sum :"+ sum);
        System.out.println("Stop ** reached..............");
    }
}