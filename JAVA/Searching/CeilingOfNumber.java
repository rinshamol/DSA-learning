public class CeilingOfNumber {
    public static void main(String[] args) {
        int[] arr = {2,3,5,9,14,19,28};
        int target = -29;
        int ceiling = search(arr, target);
        System.out.println(ceiling);
    }
    static int search(int[] arr, int target) {
        int start = 0;
        int end = arr.length -1;
        if(target > arr[end]) {
            return  -1;
        }
        while ( start <= end) {
            int mid = start + (end - start)/2;
//            if(start == end) {
//                return arr[mid + 1];
//            }
            if (target > arr[mid]) {
                start = mid + 1;
            } else if (target < arr[mid]) {
                end = mid - 1;
            } else {
                return arr[mid];
            }
        }
     return arr[start];
    }
}
