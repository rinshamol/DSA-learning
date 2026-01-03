
import java.util.Scanner;

class VolumeOfCone{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter radius and height of a cone:");
        int r = sc.nextInt();
        int h = sc.nextInt();
        double v = (1/3.0)*Math.PI*r*r*h;
        System.out.print("Volume of a cone:"+v);
    }
}