public class RichestCustomer {
    public static void main(String[] args) {
        int[][] arr = {{3,1,15}, {15,3},{3, 15}};
        int res = search(arr);
        System.out.println(res);
    }
    static int search(int[][] arr) {
        int richest = 0;
        for (int i = 0; i < arr.length; i++) {
            int sum = 0;
            for(int j = 0; j < arr[i].length; j++){
                sum += arr[i][j];
            }
            if(richest < sum) {
                richest = sum;
            }
        }
        return richest;
    }


}
