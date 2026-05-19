import java.util.Arrays;

public class RunningSum {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4};
        System.out.println(Arrays.toString(calculateSum(arr)));
    }

    static int[] calculateSum(int[] arr) {
        int sum = 0;
        int[] ans = new int[arr.length];
        for(int i = 0; i < arr.length; i++) {
            sum = sum + arr[i];
            ans[i] = sum;
        }
        return ans;
    }
}
