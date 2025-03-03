/*
Single pass scan, using stack as memory

O(N) time for scanning each character 1 at a time
O(N) memory for worst case if the stack is the size of the entire problem
*/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    let dict = {
        ']' : '[',
        '}' : '{',
        ')' : '('
    };

    for(let i = 0; i < s.length; i++){
        let curr_bracket = s[i];
        if((curr_bracket == '[') || (curr_bracket == '{') || (curr_bracket == '(')){
            stack.push(s[i]);
        }
        else{
            if(stack.pop() != dict[curr_bracket]){
                return false;
            }
        }
    }
    if(stack.length > 0){
        return false;
    }
    else{
        return true;
    }
};