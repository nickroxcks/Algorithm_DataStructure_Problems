public class IsSubsequence392 {
        public boolean isSubsequence(String s, String t) {
        if (s.length() == 0){
            return true;
        }
        if(t.length() == 0 && s.length() != 0){
            return false;
        }

        int currPos = 0;
        char currS = s.charAt(currPos);

        for(int i=0; i < t.length();i++){

            char currT = t.charAt(i);
            if(currS == currT){
                currPos++;
                if(currPos >= s.length()){
                    return true;
                }
                currS = s.charAt(currPos);
            }
        }
        return false;
    }

}
