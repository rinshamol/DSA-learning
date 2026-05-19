import java.util.ArrayList;
import java.util.List;

public class DuplicateNumber {
    public  static void  main(String[] args) {
        int[] arr = {1};
        List<Integer> ans = cyclic(arr);
        System.out.println(ans);
    }
    public static List<Integer> cyclic(int[] arr) {
        int i = 0 ;
            while (i < arr.length) {
                int correct = arr[i] - 1;
                if (arr[i] != arr[correct]) {
                    swap(arr, i, correct);
                }else {
                    i++;
                }
            }
        List<Integer> ans = new ArrayList<>();
            for(int j = 0; j < arr.length; j++) {
                if(arr[j] != j+1){
                    ans.add(arr[j]);
                }

            }
        return ans;
    }

    public  static void  swap(int[] arr, int fist, int last) {
        int temp = arr[fist];
        arr[fist] = arr[last];
        arr[last] = temp;
    }
}
