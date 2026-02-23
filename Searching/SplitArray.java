public class SplitArray {
    public static void main(String[] args) {
        int[] arr = {7,2,5,8,10};
        int m = 5;
        int sum = findMinMaxSum(arr,m);
        System.out.println(sum);
    }
    static int findMinMaxSum(int[] arr, int m){
        int start = 0;
        int end = 0;
        for(int i = 0; i < arr.length; i++) {
            start = Math.max(start, arr[i]);
            end = end + arr[i];
        }
        while (start < end) {
            int mid = start + (end - start)/2;
            int pieces = 1;
            int sum = 0;
            for(int num : arr) {
                if(sum + num > mid){
                    pieces++;
                    sum = num;
                } else  {
                    sum += num;
                }
            }
            if(pieces <= m) {
                end = mid;
            } else  {
                start = mid + 1;
            }
        }
        return start;
    }

}
