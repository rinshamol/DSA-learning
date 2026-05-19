public class BinarySearchOnInfiniteArray {
    public static void main(String[] args) {
        int[] arr = {0,1,2,3,4,5,6,6,7,8,9,13,21,22,26,33,44,55,56,56,56,67,88,99,100,200,300,400,500,600,700,800,900,1000,1200,10000,20000,100000,2120000,1000000,200000000,30000000,4000000,440000,5500000};
        int target = 26;
        int ans = searchRange(arr,target);
        System.out.println(ans);
    }

    static  int searchRange(int[] arr, int target) {
        int start = 0;
        int end = 1;
        while (target > arr[end]) {
            int newStart = end + 1;
            end = end + (end - start + 1) *2;
            start = newStart;
        }
         return search(arr,target,start,end);
    }

    static int search(int[] arr, int target, int start, int end) {
        while (start <= end) {
            int mid = start + (end - start)/2;
            if(target < arr[mid]) {
                end = mid - 1;
            } else if (target > arr[mid]) {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return  -1;
    }

}
