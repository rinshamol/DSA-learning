import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FindAllMissing {
    public static  void main(String[] args) {
        int[] arr = {1,1};
        List<Integer> ans = cyclic(arr);
        System.out.println(ans);
    }
    public static List<Integer> cyclic(int[] arr) {
        int i = 0;
        while(i<arr.length) {
            int correct = arr[i] - 1;
            if(arr[i] <= arr.length && arr[i] != arr[correct]) {
                swap(arr,i,correct);
            }else  {
                i++;
            }
        }
        List<Integer> res = new ArrayList<>();
        for (int j = 0; j < arr.length; j++) {
            if(arr[j] != j+1) {
                res.add(j+1);
            }
        }
        return res;
    }
    public static void swap(int[] arr, int first, int last) {
        int temp = arr[first];
        arr[first] = arr[last];
        arr[last] = temp;
    }
}
