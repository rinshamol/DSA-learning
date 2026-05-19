import java.util.Arrays;

public class SearchIn2DArray {
    public static void main(String[] args) {
        int[][] arr = {
                { 1,32,44,1},
                { 12,45},
                { 13,5,55},
                { 2}
        };
        int target = 5;
        int[] res = search(arr, target);
        System.out.println(Arrays.toString(res));
    }

    static int[] search(int[][] arr, int target) {
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr[i].length; j++) {
                if(arr[i][j] == target) {
                    return new int[]{i,j};
                }
            }
        }
        return  new int[]{};
    }
}
