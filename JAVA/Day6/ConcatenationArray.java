import java.util.Arrays;

public class ConcatenationArray {
    public static void main(String[] args) {
        int[] arr = {0};
        System.out.println(Arrays.toString(Concatenation(arr)));
    }
    static int[] Concatenation(int[] arr) {
        int[] res = new int[2*arr.length];
        int j = 0;
        for(int i = 0; i < res.length; i++) {
          res[i] = arr[j];
          if(i == arr.length - 1){
              j = -1;
          }
          j++;
        }
        return res;
    }

}
