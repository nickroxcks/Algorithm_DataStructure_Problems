import java.util.HashMap;
import java.util.Map;

public class IsomorphicStrings205 {

    public boolean isIsomorphic(String s, String t) {
        //Mapping of s to t
        Map<Character, Character> dicS = new HashMap<>();
        //Mapping of t to s
        Map<Character, Character> dicT = new HashMap<>();

        for(int i=0; i<s.length();i++){
            char tchar = t.charAt(i);
            char schar = s.charAt(i);

            if(dicS.containsKey(schar) ){
                if (dicS.get(schar) == tchar){
                    dicT.put(tchar, schar);
                    continue;
                }
                else{
                    return false;
                }
            }
            else{
                if(dicT.containsKey(tchar) && dicT.get(tchar) != schar){
                    return false;
                }
                else{
                    dicT.put(tchar,schar);
                }
                dicS.put(schar, tchar);

            }
        }
        return true;
    }
}
