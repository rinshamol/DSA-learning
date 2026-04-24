import java.util.Arrays;
import java.util.Optional;

public class CellsWithOddValuesInAMatrix {
    public static void main(String[] args) {
        int m = 2;
        int n = 2;
        int[][] indices = {
                {1,1},
                {0,0}
        };
        System.out.println(oddCells(m,n,indices));
        System.out.println(anotherMethod(m,n,indices));
    }
    static  int oddCells(int m, int n, int[][] indices) {
        int[][] mat = new int[m][n];

        int count = 0;
        for (int i = 0; i < indices.length; i++) {
           int r = indices[i][0];
            for(int j = 0; j < n; j++) {
                mat[r][j]++;
            }
            int c = indices[i][1];
            for(int j = 0; j < m; j++) {
                mat[j][c]++;
            }
        }
        System.out.println(Arrays.deepToString(mat));
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(mat[i][j] % 2 != 0) {
                    count++;
                }
            }
        }
         return  count;
    }

    static  int anotherMethod(int m, int n, int[][] indices) {
        int count = 0;
        int[] row = new int[m];
        int[] col =  new int[n];
        for(int x[] : indices) {
            row[x[0]]++;
            col[x[1]]++;
        }
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++){
                if((row[i]+col[j]) % 2 != 0) {
                    count++;
                }
            }
        return count;
    }
}
