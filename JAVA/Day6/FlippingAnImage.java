import java.util.Arrays;

public class FlippingAnImage {
    public static void main(String[] args) {
        int[][] image = {
                {1,1,0,0},
                {1,0,0,1},
                {0,1,1,1},
                {1,0,1,0}
        };
        int[][] ans = flipAndInvertImage(image);
        System.out.println(Arrays.deepToString(ans));
    }

    static int[][] flipAndInvertImage(int[][] image) {
        int n = image.length;
        int[][] result = new int[n][n];
        for(int i = 0; i < n; i++) {
            int k = n-1;
            for (int j = 0; j<n; j++) {

                if(image[i][k] == 0){
                    result[i][j] = 1;
                } else {
                    result[i][j] = 0;
                }
                k--;

            }
        }
        return  result;
    }
}
