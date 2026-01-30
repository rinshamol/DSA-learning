class Fibonacci {
    public static void main(String[] args) {
        int num = 50;
        int result = fibonacciNum(num);
        System.out.println(result);
    }

    static  int fibonacciNum(int index) {
        if(index < 2) {
            return index;
        }

        return fibonacciNum(index-1) + fibonacciNum(index-2);
    }
}