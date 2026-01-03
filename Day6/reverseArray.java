
import java.util.Arrays;
import java.util.Scanner;

public class reverseArray{
public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the array size:");
    int n = sc.nextInt();
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
        arr[i] = sc.nextInt();
    }
    System.out.println(Arrays.toString(arr));
    int start = 0;
    int end = arr.length - 1;
    while(start < end){
        swap(arr,start,end);
        start++;
        end--;
    }
    System.out.println(Arrays.toString(arr));
}
 static void swap(int[] arr, int start, int end){
    int temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
}
}