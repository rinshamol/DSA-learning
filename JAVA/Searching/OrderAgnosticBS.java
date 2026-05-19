public class OrderAgnosticBS {
    public static void main(String[] args) {
//        int[] arr = {-1,0,2,4,13,19,24,35,47,66,89,97};
        int[] arr2 = {98,87,76,66,54,33,21,10,8,1,-22};
        int target = -22;
        int res = search(arr2, target);
        System.out.println(res);
    }
    static int search(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;
        //find the order of the sorted array
        boolean isAsc = arr[start] < arr[end];

        while(start <= end) {
            int mid = start + (end - start) / 2; // to avoid int size exceeding
            if(target == arr[mid]){
                return  mid;
            }
            if(isAsc) {
                if (target > arr[mid]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            } else {
                if (target < arr[mid]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        return -1;
    }
}
