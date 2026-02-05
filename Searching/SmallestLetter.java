public class SmallestLetter {
    public static void main(String[] args) {
        char[] arr = {'c','f','h','j','m'};
        char target = 'h';
        char ans = search(arr,target);
        System.out.println(ans);

    }
    static char search(char[] arr, char target) {
        int start = 0;
        int end = arr.length - 1;
        while(start <= end) {
            int mid = start + (end - start)/2;
//            if(target == arr[mid]) {
//                return arr[mid+1];
//            }
            if(target < arr[mid]) {           // we need to check == also thats why we check < after in the else which for both >=
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        System.out.println(start % arr.length);
        return  arr[start % arr.length];
    }
}
