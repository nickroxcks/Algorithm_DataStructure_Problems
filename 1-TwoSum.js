/* My Solution
O(n) time
O(n) memory
*/
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = {};
    for (let i = 0; i<nums.length;i++){
        let currValue = nums[i];
        if(map[currValue] != undefined){
            return [i, map[currValue]];
        }
        else{
            map[target-currValue] = i
        }
    }
    return [];
};

