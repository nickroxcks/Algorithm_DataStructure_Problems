/* My Solution
O(m+n) time
O(m) Space complexity
Storing a copy of the first array required m extra memory
*/
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  let num1copy = [...nums1];
  let p1 = 0;
  let p2 = 0;
  if (m === 0) {
    for (let i = 0; i < n; i++) {
      nums1[i] = nums2[i];
    }
    return;
  }
  if (n === 0) {
    return;
  }

  for (let i = 0; i < m + n; i++) {

    if ((num1copy[p1] <= nums2[p2] || nums2[p2] === undefined) && p1 < m) {
      nums1[i] = num1copy[p1];
      p1++;
    } else {
      nums1[i] = nums2[p2];
      p2++;
    }
  }
};

/*LeetCode Solution
O(m+n) time
O(1) Space complexity
*/
var mergeOpimal = function(nums1, m, nums2, n) {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;
    
    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
};
/*
let nums1 = [0];
let nums2 = [1];
let m = 0;
let n = 1;
merge(nums1,m,nums2,n);
console.log(nums1);
*/
/*
let nums1 = [1, 2, 3, 20, 28, 39, 999, 0, 0, 0, 0, 0];
let nums2 = [2, 5, 6, 20, 39];
let m = 7;
let n = 5;
merge(nums1, m, nums2, n);
console.log(nums1);


*/

/*Debug logs
    console.log("i:", i);
    console.log("p1:", p1);
    console.log("p2:", p2);
    console.log("num1copy element:", num1copy[p1]);
    console.log("num1copy:", num1copy);
    console.log("num2 element:", nums2[p2]);
    console.log("num1 before", nums1);
*/
