import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> dic = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if(dic.containsKey(complement)){
                return new int[] {i, dic.get(complement)};
            }
            else{
                dic.put(target - complement, i);
            }
        }
        return new int[] {};
    }

    public static void  main(String[] args){
        int[] arr = {2,7,11,15};
        System.out.println(Arrays.toString(twoSum(arr,9)));
    }
}
