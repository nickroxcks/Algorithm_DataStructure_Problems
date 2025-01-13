/*My Solution

Linear search with hash table
O(n) time, O(n) memory

Other solutions including pre-sorting first O(nlogn) time O(1) memory

Optimal solution is Boyer-Moore Voting Algorithm
O(n) time O(1) memory
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let map = {};
    let n = nums.length
    for(let i = 0; i < n;i++){
        let num = nums[i]
        if(map[num]!== undefined){
            map[num] = map[num] + 1;
            if(map[num] > n/2){
                return num
            }
        }
        else{
            map[num] = 1;
        }
    }
    return nums[0];
};

let nums = [2, 1, 1, 1, 3];

console.log(majorityElement(nums));