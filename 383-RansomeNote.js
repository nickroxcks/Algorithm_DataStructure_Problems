/*
My Solution: 1 hashmap, scan both note and magazine

O(n) time
O(26) = O(1) memory

We first scan the magazine and store the number of occurences for each letter in a hashmap, then
scan the ransom note and see if we have enough letters in the hashmap.

There are only 26 letters in the alphabet, meaning at most we have 26 letters in the dictionary.
*/


/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    let dic = {};

    for(let i=0;i<magazine.length;i++){
        if(dic[magazine[i]]){
            dic[magazine[i]] = dic[magazine[i]] + 1
        }
        else{
            dic[magazine[i]] = 1;
        }
    }

    for(let j=0;j<ransomNote.length;j++){
        if(!dic[ransomNote[j]] || dic[ransomNote[j]]  == 0){
            return false;
        }
        else{
            dic[ransomNote[j]] = dic[ransomNote[j]] - 1;
        }
    }
    return true;
};