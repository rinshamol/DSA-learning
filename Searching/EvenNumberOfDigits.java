public class EvenNumberOfDigits {
    public static void main(String[] args) {
        int [] arr = {12,324,2,6,-4356};
        int res = search(arr);
        int res2 = search2(arr);
        System.out.println(res + " - " + res2);

    }
    // method 1- by converting int to string and calculated the length is even or not for each elements
    static int search(int[] arr) {
        int count = 0;
        for(int a : arr) {
            if(a < 0) {
                a *= -1;
            }
            String temp = String.valueOf(a);
            if(temp.length() % 2 == 0) {
                count++;
            }
        }
        return count;
    }
    // method 2 - manual method
    static int search2(int[] arr) {
        int count = 0;
        for(int a : arr) {
            if(a < 0) {
                a *= -1;
            }
            int noOfDigits = digits2(a);
            if(noOfDigits % 2 == 0) {
                count++;
            }
        }
        return count;
    }

    static int digits(int a) {
        int count = 0;
        while (a > 0) {
            a = a/10;
            count++;
        }
        return count;
    }

    static int digits2(int a) {
        if(a < 0) {
            a *= -1;
        }
        return (int)(Math.log10(a)) + 1;
    }
}
