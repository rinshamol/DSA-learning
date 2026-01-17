import java.util.Arrays;

public class DuplicateNumber {
    public  static void  main(String[] args) {
        int[] arr = {1,3,2,2,4};
        int num = cyclic(arr);
        System.out.println(num);
    }
    public static int cyclic(int[] arr) {
        int i = 0 ;
            while (i < arr.length) {
                if(arr[i] != i+1) {
                int correct = arr[i] - 1;
                if (arr[i] != arr[correct]) {
                    swap(arr, i, correct);
                } else {
                   return arr[i];
                }
            }else {
                    i++;
                }
        }
        return -1;
    }

    public  static void  swap(int[] arr, int fist, int last) {
        int temp = arr[fist];
        arr[fist] = arr[last];
        arr[last] = temp;
    }
}
