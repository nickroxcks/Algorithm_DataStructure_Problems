/**
 * @param {number} x
 * @return {number}
 * 
 */
/*My Solution
Binary Search

O(logn) time
O(1) memory
*/

var mySqrt = function(x) {
    if(x < 2){
        return x;
    }

    let num = 0;
    let pivot = 2;
    let left = 2;
    let right = Math.ceil(x/2);

    while(left<=right){

        pivot =Math.ceil( left + (right - left)/2);
        num = pivot * pivot;
        
        //if the squared value is greater then x, wthe number we found is too bug
        //move right l below the pivot. The pivot
        if(num > x){
            right = pivot -1;
        }
        else if(num < x){
            left = pivot + 1
        }
        else{
            return pivot
        }

        
    }
    return right;

};

/* Cheating Solution
This solution uses non elementary operations to calculate the solution.
We know:
a2 ≤ x < (a+1)^2

So:
sqrt(x) = e ^ (0.5 * log(x))
*/



var mySqrtLeetCode = function(x) {
    if (x < 2) return x;

    let left = Math.floor( Math.E ** (0.5 * Math.log(x)));
    let right = left + 1;
    return right * right > x ? left : right;

}
console.log(mySqrt(10));
console.log(mySqrtLeetCode(10));