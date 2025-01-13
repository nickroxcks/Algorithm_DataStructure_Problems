/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    //left and right refer to the index. Guarantee nums.length >=1
    let left = 0;
    let right = 0;
    let k = 0;
    let prev = null
    for(let i=0;i<nums.length;i++){

        let curNum = nums[i];

        //check if new number. If not, move on to next iteration
        if(prev === null || (curNum > prev)){
            prev = curNum;
            k++;
            nums[left] = curNum;

            //adjust left pointer. Make sure we are not at the end of the array
            if(nums[left + 1] != undefined){
                left++;
            }
        }
    }
    return k;
};

let nums = [1,2,3,4,5,6,7,8,9,20];

console.log(removeDuplicates(nums),nums);