/*My Solution
O(2n) time, O(1) memory

*/
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    //1 <= digits.length <= 100
    // /0 <= digits[i] <= 9
    let lastIndex = digits.length-1;
    if(digits[lastIndex] != 9){
        let val = digits[lastIndex];
        digits[lastIndex] = val + 1
        return digits;
    }

    for (let i = lastIndex; i>=0; i--){
        if(digits[i] === 9 && i!=0){
            digits[i] = 0;
        }
        else if (digits[i] < 9){
            let num = digits[i];
            digits[i] = num + 1
            break;
        }

        else{
            digits[i] = 0;
            digits.unshift(1);
        }
    }
    return digits;
};

var plusOneFaster = function(digits) {
    //1 <= digits.length <= 100
    // /0 <= digits[i] <= 9
    let lastIndex = digits.length-1;
    if(digits[lastIndex] != 9){
        let val = digits[lastIndex];
        digits[lastIndex] = val + 1
        return digits;
    }
    
    for (let i = lastIndex; i>=0; i--){
        if(digits[i] === 9 && i!=0){
            digits[i] = 0;
        }
        else if (digits[i] < 9){
            let num = digits[i];
            digits[i] = num + 1
            break;
        }

        else{
            digits[i] = 0;
            digits.unshift(1);
        }
    }
    return digits;
};
let digits = [9,9,9,9]
console.log(plusOne(digits));
//979
//999