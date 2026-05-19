public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = {-1,0,2,4,13,19,24,35,47,66,89,97};
        int target = 66;
        int res = search(arr, target);
        System.out.println(res);
    }
    static int search(int[] arr, int target) {
        int start = 0;
        int end = arr.length-1;
        while(start <= end) {
            int mid = start + (end - start) / 2; // to avoid int size exceeding
            if(target > arr[mid]) {
                start = mid + 1;
            } else if(target < arr[mid]) {
                end = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
