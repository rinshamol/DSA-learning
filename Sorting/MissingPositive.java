public class MissingPositive {
    public  static  void main(String[] args) {
        int[] arr = {-1,1};
        int num = CyclicSort(arr);
        System.out.println(num);

    }
    public  static  int CyclicSort(int[] arr) {
        int i = 0;
        while (i< arr.length) {
            int correct = arr[i] - 1;
            if(arr[i] > 0 && arr[i] < arr.length && arr[i] != arr[correct]){
                swap(arr,i,correct);
            }else  {
                i++;
            }
        }
        for(int j = 0; j < arr.length; j++) {
            if(arr[j] != j+1) {
                return j+1;
            }
        }
        return arr.length+1;
    }
    static void  swap(int[] arr, int first, int last) {
        int temp = arr[first];
        arr[first] = arr[last];
        arr[last] = temp;
    }
}
