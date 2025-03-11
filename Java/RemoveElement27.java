/*
Algorithm: Two pointer linear scan
O(n) time
O(1) memory

Have a slow pointer p1 and a fast pointer p2. Have p2 increase with every iteration and when nums[p2]!= val,
update the value at position p1, and move p1 to the next element.

Since p1 starts at index 0, the solution is simply to return p1
 */

public class RemoveElement27 {
    public int removeElement(int[] nums, int val) {
        int p1 = 0;
        int sol;
        for(int p2=0;p2<nums.length;p2++){
            if(nums[p2] == val){
                continue;
            }
            else{
                nums[p1] = nums[p2];
                p1++;
            }
        }
        return p1;
    }
}
