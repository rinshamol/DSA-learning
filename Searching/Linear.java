public class Linear {
        public static void  main(String[] args) {
            int[] arr = {34,55,12,20,22};
            int res = search(arr, 22);
            System.out.println(res);
        }

        static int search(int[] arr, int target) {
            if(arr.length == 0) {
                return  -1;
            }
            for (int i = 0; i < arr.length; i++) {
                if(arr[i] == target) {
                    return i;
                }
            }
            return -1;
        }
}
