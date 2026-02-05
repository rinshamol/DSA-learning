import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RangeOfNumber {
    public static void main(String[] args) {
        int[] arr = {5,8,8,8,8,10};
        int target = 8;
        List<Integer> range = search(arr,target);
        System.out.println(range);
    }

    static List<Integer> search(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;
        int flag = 0;
        List<Integer> res = new ArrayList<>();
        //BS-start range
        while (start <= end) {
            int mid = start + (end - start)/2;
            if(target == arr[mid] && start == end){
                res.add(0, mid);
            }
            if(target <= arr[mid]) {
                end = mid - 1;
            }else  {
                start = mid + 1;
            }

        }

        //BS-end range
        start = 0;
        end = arr.length - 1;
        while (start <= end) {
            int mid = start + (end - start)/2;
            if(target == arr[mid] && start == end){
                res.add(1, mid);

            }
                if(target >= arr[mid]) {
                    start = mid + 1;
                }else  {
                    end = mid + 1;
                }


        }
        if(flag == 1) {
            res.add(1, end);
        }
        if(res.isEmpty()) {
            res.add(0,-1);
            res.add(1,-1);
        }
        return res;
    }
}
