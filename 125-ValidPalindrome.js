/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const re = new RegExp("^[A-Za-z0-9]*$");

  //console.log(re.test(s));
  //lowercase al letters

  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    let leftVal = s[left];
    let rightVal = s[right];

    if (!re.test(leftVal)) {
      left++;
      continue;
    }
    if (!re.test(rightVal)) {
      right--;
      continue;
    }
    if (leftVal.toLowerCase() != rightVal.toLowerCase()) {
      return false;
    }
    left++;
    right--;
  }

  return true;
};

//console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome("Rac:::::e:car"));
