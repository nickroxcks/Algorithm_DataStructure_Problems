/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  //strs guaranteed 1 element, so this is safe
  let minStr = strs[0];

  if(strs.length===1){
    return minStr;
  }
  for (let i = 1; i < strs.length; i++) {
    let currStr = strs[i]; //the current string in array we are looking at
    if (currStr.length === 0) {
      //if we find an empty stirng, there is no min prefix so return empty
      return "";
    } else {
      //otherwise, lets look at the current string and check how many chars are the same as the current minStre
      let curMin = "";
      for (let j = 0; j < currStr.length; j++) {
        if (currStr.at(j) != undefined && currStr.at(j) === minStr.at(j)) {
          curMin = curMin + currStr.at(j);
        } else {
          break;
        }
      }
      if (curMin.length === 0) {
        return "";
      } else if (curMin.length < minStr.length) {
        minStr = curMin;
      }
    }
  }
  return minStr;
};
let strs = ["flower", "flow", "flight"];
console.log(longestCommonPrefix(strs));
