import java.util.HashMap;
import java.util.Map;

public class MajorityElement169 {

    public int majorityElement(int[] nums) {
        int maj_element = 0;
        int max_count =  0;
        Map<Integer, Integer> dic = new HashMap<>();
        for (int curr_num : nums) {
            int curr_occurences;
            if (dic.containsKey(curr_num)) {
                curr_occurences = dic.get(curr_num) + 1;
                dic.put(curr_num, curr_occurences);
            } else {
                curr_occurences = 1;
                dic.put(curr_num, curr_occurences);
            }

            if (curr_occurences >= max_count) {
                max_count = curr_occurences;
                maj_element = curr_num;
            }
        }
        return maj_element;
    }
}
