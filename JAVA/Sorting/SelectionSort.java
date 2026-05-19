import java.util.Arrays;

class SelectionSort{
    public static void main(String[] args) {
        int [] arr = {-2,-32,0,5,3};
        selectionSmall(arr);
//      selectionLarge(arr);
        System.out.println(Arrays.toString(arr));
    }
    //sorting largest elements 1st
    static  void selectionLarge(int[] arr) {
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
    //sorting smallest elements 1st
    static  void  selectionSmall(int[] arr) {
        for(int i = 0; i < arr.length; i++) {
            int first = i;
            int last = arr.length-1;
            int min = getMinIndex(arr,first, last);
            swap(arr,first,min);
        }
    }

    static int getMinIndex(int[] arr, int first, int last) {
        int min = first;
        for(int i = first; i < arr.length-1; i++) {
            if(arr[min] > arr[i]) {
                min = i;
            }
        }
        return min;
    }
}