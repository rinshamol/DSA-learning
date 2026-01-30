
import java.util.ArrayList;
import java.util.List;

class SearchChar {
    public static void main(String[] args) {
        String str = "Rinsha Aadhil";
        char c = ' ';
        List<Integer> res = search(str, c);

        System.out.println(res);
        
    }
    static  List<Integer> search(String str, char target) {
        List<Integer> list = new ArrayList<>();
        for(int i = 0 ; i < str.length(); i++){
            if(str.charAt(i) == target) {
                list.add(i);
            }
        }
        return list;
    }
}