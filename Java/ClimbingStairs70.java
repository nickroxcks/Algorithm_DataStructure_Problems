import java.util.HashMap;
import java.util.Map;

public class ClimbingStairs70 {

        public int climbStairs(int n) {

        if(n == 1){
            return 1;
        }
        if (n==2){
            return 2;
        }

        Map<Integer, Integer> dic = new HashMap<>();
        dic.put(1,1);
        dic.put(2,2);

        for(int i=3; i <= n; i++){
            dic.put(i, dic.get(i-1) + dic.get(i-2));
        }

        return dic.get(n-1) + dic.get(n-2);
    }

}
