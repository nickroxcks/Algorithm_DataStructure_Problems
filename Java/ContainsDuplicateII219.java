import java.util.HashMap;
import java.util.Map;

public class ContainsDuplicateII219 {

    public boolean containsNearbyDuplicate(int[] nums, int k) {

        Map<Integer, Integer> dic = new HashMap<>();

        for(int i=0; i< nums.length;i++){

            int currNum = nums[i];

            if(!dic.containsKey(currNum)){
                dic.put(currNum,i);
            }
            else{
                int j = dic.get(currNum);
                if(Math.abs(i-j) <=k){
                    return true;
                }
                dic.put(currNum,i);
            }
        }
        return false;
    }
}
