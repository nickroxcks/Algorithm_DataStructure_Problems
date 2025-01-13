/*My Solution
O(n) time, O(1) space

Hard coded each case in order to avoid the use of hash map. 
Generally hash maps are O(1) lookup but very rare worst case is possible for O(n)
My solution avoids the use of hashmap to essure consistent results
*/

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const I = 1;  //special cases
    const V = 5
    const X = 10;  //speacial cases
    const L = 50;
    const C = 100;  //speacial cases
    const D = 500;
    const M = 1000;
    let totalsum = 0;
    let skip = false;
    let numletters = s.length;
    for(let i=0; i < s.length;i++){
        let curLetter = s[i];
        if(skip){
                skip = false;
                continue;
        }
            if (curLetter === 'I'){
                if( i+1<numletters && s[i+1] == 'V'){
                    totalsum = totalsum + 4;
                    skip = true;
                }
            
                else if (i+1<numletters && s[i+1] == 'X'){
                    totalsum = totalsum + 9;
                    skip = true;
                }
                else {
                    totalsum = totalsum + 1;
                }
            }
            else if (curLetter === 'X'){
                if (i+1<numletters && s[i+1] === 'L'){
                    totalsum = totalsum + 40;
                    skip = true;
                }
                else if( i+1<numletters && s[i+1] == 'C'){
                    totalsum = totalsum + 90;
                    skip = true;
                }
                else{
                    totalsum = totalsum + 10;
                }
            }

            else if (curLetter == 'C'){
                if (i+1<numletters && s[i+1] == 'D'){
                    totalsum = totalsum + 400
                    skip = true
                }
                else if( i+1<numletters && s[i+1] == 'M'){
                    totalsum = totalsum + 900
                    skip = true

                }
                else{
                    totalsum = totalsum + 100
                }
            }
            else if( curLetter == 'V'){
                totalsum = totalsum + 5
            }
            else if( curLetter == 'L'){
                totalsum = totalsum + 50
            }
            else if( curLetter == 'D'){
                totalsum = totalsum + 500
            }
            else{
                totalsum = totalsum + 1000
            }

    }
    return totalsum;
}


/* Leetcode Solution

Uses disctionaries to make the solution cleaner. Runs the risk of hash collision but in general very good solution

O(n) time O(n) space
*/
/**
 * @param {string} s
 * @return {number}
 */
var romanToIntOptimal = function(s) {
    const legend = {
  I:1,
  V:5,
  X:10,
  L:50,
  C:100,
  D:500,
  M:1000
};
let total = 0;

for (let i = 0; i < s.length; i++) {
  if (legend[s[i]] < legend[s[i+1]]) {
    total += legend[s[i+1]] - legend[s[i]];
    i++;
  } else {
    total += legend[s[i]];
  }
}

return total;
}