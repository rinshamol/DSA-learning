
import java.util.Arrays;

class SelectionSort{
    public static void main(String[] args) {
        int [] arr = {-2,-32,0,5,3};
       selection(arr);
        System.out.println(Arrays.toString(arr));
    }

    static  void selection(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int last = arr.length - i - 1;
            int maxIndex = getMaxIndex(arr, 0, last);   
            swap(arr, maxIndex, last);
        }
    }

    static int getMaxIndex(int[] arr, int start, int last){
        int max = start;
        for (int i = 0; i <= last; i++) {
            if(arr[max] < arr[i]) {
                max = i;
            }
        }
        return max;
    }

    static void swap(int[] arr, int max, int last){
        int temp = arr[max];
        arr[max] = arr[last];
        arr[last] = temp;
    }
}