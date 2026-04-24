import java.util.Arrays;
import java.util.List;

public class CountMatches {
    public static void main(String[] args) {
        List<List<String>> mat = Arrays.asList(
                Arrays.asList("phone", "blue", "pixel"),
                Arrays.asList("computer", "silver", "lenovo"),
                Arrays.asList("phone", "gold", "iphone")
        );
        String ruleKay = "type";
        String ruleValue = "phone";
        System.out.println(countMachers(mat,ruleValue,ruleKay));
    }
    static int countMachers(List<List<String>> items,String ruleValue, String ruleKey) {
        int count = 0;
        int col;
        if(ruleKey.equals("type")) {
            col = 0;
        } else if ( ruleKey.equals("color")) {
            col = 1;
        } else  {
            col = 2;
        }

        for(int i = 0; i < items.size(); i++) {
            if (ruleValue == items.get(i).get(col)) {
                count++;
            }
        }
        return count;
    }
}
