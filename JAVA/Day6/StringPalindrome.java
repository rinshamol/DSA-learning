public class StringPalindrome {
    public static void main(String[] args) {
        String str = "rinir";
        System.out.println(palindrome(str.toLowerCase()));
    }

    static boolean palindrome(String str) {
        int start = 0;
        int end = str.length() - 1;
        while(start<=end) {
            if(str.charAt(start) != str.charAt(end)) {
                return false;
            }
            start ++;
            end --;
        }
        return true;
    }
}
