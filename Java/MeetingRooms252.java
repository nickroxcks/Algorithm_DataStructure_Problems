import java.util.Arrays;
import java.util.Comparator;

/**
 * O(nlongn) runtime, O(n) memory
 * Sort the array, then check if the current item is greater than the next
 */
public class MeetingRooms252 {
        public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        for(int i=0; i < intervals.length -1; i++){

            if(intervals[i][1] > intervals[i + 1][0]){
                return false;
            }
        }
        return true;
    }
}
