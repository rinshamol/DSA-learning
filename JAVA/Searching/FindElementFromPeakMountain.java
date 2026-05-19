public class FindElementFromPeakMountain {
    public static void main(String[] args) {
        int[] arr = {0,2,4,6,7,5,3,1};
        int target = 10;
        int res = search(arr, target);
        System.out.println(res);
    }

    static int search(int[] arr, int target) {
        int peak = peakElement(arr);
        if(target == arr[peak]) {
            return peak;
        }
        int firstHalf = orderAgnosticSearch(arr,target,0,peak-1,true);
        if(firstHalf != -1){
            return firstHalf;
        }
        return orderAgnosticSearch(arr,target,peak+1,arr.length-1,false);
    }

    static int peakElement(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        while (start < end) {
            int mid = start + (end - start)/2;
            if(arr[mid] > arr[mid + 1]) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return  start;
    }

    static int orderAgnosticSearch (int[] arr, int target, int start, int end, boolean isFirst) {
        while (start <= end){
            int mid = start + (end - start);
            if(isFirst) {
                if(target > arr[mid]) {
                    start = mid + 1;
                } else if(target < arr[mid]) {
                    end = mid - 1;
                } else {
                    return  mid;
                }
            } else {
                if(target < arr[mid]) {
                    start = mid + 1;
                } else if(target > arr[mid]) {
                    end = mid - 1;
                } else {
                    return  mid;
                }
            }
        }
        return  -1;
    }
}
