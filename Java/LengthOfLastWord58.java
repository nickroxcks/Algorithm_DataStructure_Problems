public class LengthOfLastWord58 {

    public int lengthOfLastWord(String s) {
        int num_letters = 0;
        int len = s.length();

        for(int i = len - 1; i >= 0;i--){
            char cur_letter = s.charAt(i);
            if(cur_letter == ' ' && num_letters >0){
                break;
            }
            else if (cur_letter == ' ' && num_letters == 0){
                continue;
            }
            else{
                num_letters++;
            }

        }

        return num_letters;
    }
}
