public class ValidPalindrome125 {

    public boolean isPalindrome(String s) {

        //hard code the null case
        if (s.isEmpty()) {
            return true;
        }
        int left = 0;
        int right = s.length() - 1;

        while(left <= right) {
            char currLeft = s.charAt(left);
            char currRight = s.charAt(right);

            //Check if any of the pointers are pointing to a non-alphanumeric and if so skip
            if (!Character.isLetterOrDigit(currLeft )) {
                left++;
            }

            else if(!Character.isLetterOrDigit(currRight)) {
                right--;
            }

            //Now check if the pointers have the same char. If not, return false
            else {
                if (Character.toLowerCase(currLeft) != Character.toLowerCase(currRight)) {
                    return false;
                }
                left++;
                right--;
            }
        }
        return true;
    }
}
