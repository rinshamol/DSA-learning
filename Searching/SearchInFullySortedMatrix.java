import java.util.Arrays;

public class SearchInFullySortedMatrix {
    public static void main(String[] args) {
        int[][] matrix = {
                {1,  2,  3,  4 },
                {5,  6,  7,  8 },
                {9, 10, 11,  12},
                {13, 14, 15, 16}
        };
        int target = 33;
        int[] ans  = search(matrix, target);
        System.out.println(Arrays.toString(ans));
    }
    static int[] search(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        if(rows == 1) {
            return bSearch(matrix,target,0,0,cols-1);
        }
        int rStart = 0;
        int rEnd = rows -1;
        int cMid = cols/2;

        while (rStart < (rEnd - 1)) {
            int mid = rStart + (rEnd - rStart)/2;
            if(target == matrix[mid][cMid]) {
                return new int[] {mid,cMid};
            }
            if(target > matrix[mid][cMid]){
                rStart = mid;
            }else {
                rEnd = mid;
            }
        }
        if(target == matrix[rStart][cMid]) {
            return new int[] {rStart, cMid};
        }
        if(target == matrix[rStart+1][cMid]) {
            return new int[] {rStart + 1, cMid};
        }
        if(target < matrix[rStart][cMid]){
            return bSearch(matrix,target,rStart,0,cMid-1);
        }
        if(target > matrix[rStart][cMid] && target <= matrix[rStart][cols - 1]){
            return bSearch(matrix,target,rStart,cMid + 1,cols - 1);
        }
        if(target < matrix[rStart + 1][cMid]){
            return bSearch(matrix,target,rStart + 1,0,cMid-1);
        } else  {
            return bSearch(matrix,target,rStart + 1,cMid + 1,cols - 1);
        }

    }

    static int[] bSearch(int[][] matrix, int target, int row, int cStart, int cEnd) {
        while (cStart <= cEnd) {
            int mid = cStart + (cEnd- cStart)/2;
            if(target == matrix[row][mid]) {
                return new int[] {row,mid};
            }
            if(target > matrix[row][mid]) {
                cStart = mid + 1;
            }else  {
                cEnd = mid - 1;
            }
        }
        return new int[]{-1,-1};
    }


}
