public class FloorOfNumber {
    public static void main(String[] args) {
        int[] arr = {2,3,5,9,14,19,28};
        int target = 1;
        int floor = search(arr, target );
        System.out.println(floor);
    }

    static  int search(int[] arr, int target) {
        int start = 0;
        int end = arr.length -1;
        if(target < arr[start]) {
            return -1;
        }
        while(start <= end) {
            int mid = start + (end - start)/2;
            if(target == arr[mid]) {
                return arr[mid];
            }
            if(target > arr[mid]) {
                start = mid + 1;
            } else  {
                end = mid - 1;
            }
        }
        return arr[end];
    }

}

