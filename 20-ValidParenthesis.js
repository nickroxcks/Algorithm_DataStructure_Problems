/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let dict = {
        '{' : '}',
        '[' : ']',
        '(': ')'
    }
    let stack = []
    stack.push(s.at(0));
    
    for(let i = 1; i< s.length; i++){
        let curBracket = s.at(i);
        if ((curBracket === '{') || (curBracket === '(') || (curBracket === '[')){
            stack.push(curBracket);
        }
        else{
            let poppedBracket = stack.pop();
            if (dict[poppedBracket] != curBracket){
                return false
            }
        }
    }
    if(stack.length === 0){
        return true;
    }
    else{
        return false;
    }
};