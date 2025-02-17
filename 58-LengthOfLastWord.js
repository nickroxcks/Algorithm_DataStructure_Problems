/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let p = s.length - 1;
    let wordlen = 0;

    while(p >= 0){
        if(s[p] != " " && wordlen >=0){
            wordlen++;
        }
        else if(s[p] == " " && wordlen > 0){
            return wordlen;
        }
        p--;
    }
    return wordlen;
};