/*
O(n*m) time
O(1) memory
n = problem size
m = length of haystack

This is a brute force approach as we are performing nested for loop approach, where for each character in the haystack,
we are checking to see if that characters will lead to a substring that matches needle

This approach is performed rather then a single one pass loop on order to catch special edge cases such as the word
"mississippi", where needles such as "issip" can appear inside other needles

28-FindTheIndexofFirstOccurenceString.py
 */

public class FindTheIndexofFirstOccurenceString28 {
    public int strStr(String haystack, String needle) {
        int m = needle.length();
        int n = haystack.length();

        for(int i = 0; i < n + 1 - m; i++){
            for (int j=0;j<m;j++){
                if(haystack.charAt(i+j) != needle.charAt(j)){
                    break;
                }
                if(j == m -1){
                    return i;
                }
            }
        }
        return -1;
    }

}
