import java.util.Arrays;

public class SearchRange {
    public static void main(String[] args) {
        int[] arr = {5,7,7,8,8,10};
        int target = 11;
        int[] res = search(arr,target);
        System.out.println(Arrays.toString(res));
    }

    static int[] search(int[] arr, int target) {
        int[] res = {-1,-1};
        res[0] = bSearch(arr,target,true);
        if(res[0] != -1){
            res[1] = bSearch(arr,target,false);
        }
        return res;
    }
    static  int bSearch(int[] arr, int target, boolean isFirstRange) {
        int res = -1;
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            int mid = start + (end - start)/2;
            if(target < arr[mid]) {
                end = mid - 1;
            } else if (target > arr[mid]) {
                start = mid + 1;
            } else {
                res = mid;
                if(isFirstRange){
                    end = mid - 1;
                } else  {
                    start = mid + 1;
                }
            }
        }
        return res;
    }

}
