import java.util.HashMap;
import java.util.Map;

public class ValidAnagram242 {
    public boolean isAnagram(String s, String t) {

        Map<Character, Integer> dic = new HashMap<>();

        if(s.length() != t.length()){
            return false;
        }

        //build dictionary of t
        for(int i=0; i< t.length();i++){
            char currLetter = t.charAt(i);

            if(!dic.containsKey(currLetter)){
                dic.put(currLetter,1);
            }
            else{
                int newVal = dic.get(currLetter) + 1;
                dic.put(currLetter, newVal);
            }
        }

        for(int j=0; j<s.length(); j++){
            char currLetter = s.charAt(j);
            if(dic.containsKey(currLetter) && (dic.get(currLetter) > 0)){
                int newVal = dic.get(currLetter) - 1;
                dic.put(currLetter,newVal);
            }
            else{
                return false;
            }
        }
        return true;
    }
}
