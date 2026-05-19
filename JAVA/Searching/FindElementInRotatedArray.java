public class FindElementInRotatedArray {
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5,6};
        int target =  5;
        int res = search(arr,target);
        System.out.println(res);
    }

    static int search(int[] arr, int target) {
        int pivot = findPivot(arr);
        if(pivot == -1) {
            return bSearch(arr,target,0, arr.length - 1);
        }
        if( arr[pivot] == target) {
            return  pivot;
        }
        int first = bSearch(arr, target, 0, pivot - 1);
        if(first != -1){
            return  first;
        }
        return bSearch(arr, target, pivot + 1, arr.length);

    }

    static int findPivot(int[] arr) {
        int start = 0;
        int end = arr.length -1;
        while (start < end) {
            int mid = start + (end - start)/2;
            if(mid < end && arr[mid] > arr[mid + 1]) {
                return mid;
            }
            if(mid > start && arr[mid] < arr[mid - 1]) {
                return mid-1;
            }

            if( arr[start] >= arr[mid]) {
                end = mid - 1;
            }else  {
                start = mid + 1;
            }
        }
         return -1;
    }

    static int bSearch(int[] arr, int target, int start, int end){
        while (start <= end) {
            int mid = start +  (end -  start)/2;
            if( target > arr[mid]) {
                   start = mid + 1;
            } else if(target < arr[mid])  {
                end = mid - 1;
            } else {
                return mid;
            }
        }
         return  -1;
    }
}


