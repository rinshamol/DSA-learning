import  java.util.Scanner;
public  class Largest{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Two numbers :");
        int a = sc.nextInt();
        int b = sc.nextInt();
        if(a > b){
            System.err.println(a + " is largest");
        }else if(a < b){
            System.err.println(b + " is largest");
        }else{
            System.err.println(a + " and " + b + " are Equal");
        }
    }
}