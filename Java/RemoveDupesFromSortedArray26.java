public class RemoveDupesFromSortedArray26 {
    public int removeDuplicates(int[] nums) {
        int left = 0;
        int right = 0;

        for(int curr_num : nums){

            //hard code the beginning edge case
            if(left == 0){
                left++;
                right++;
                continue;
            }

            //in this case, we have a duplicate
            else if(curr_num == nums[left-1]){
                right++;
            }

            //we have a new number
            else{
                nums[left] = nums[right];
                right++;
                left++;
            }
        }
        return left;
    }

}
