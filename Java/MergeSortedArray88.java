/*
My Solution: 3 pointers single scan, and make copy of nums1
O(n+m) time, O(n+m) memory
 */
public class MergeSortedArray88 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int[] nums1Copy = nums1.clone();

        int p1 = 0;
        int p2 = 0;

        for (int p = 0; p < m + n; p++) {

            //double check boundaries edge case, as p2 is likely smaller
            if (p2 >= n || (p1 < m && nums1Copy[p1] < nums2[p2])) {
                nums1[p] = nums1Copy[p1];
                p1++;
            } else {
                nums1[p] = nums2[p2];
                p2++;
            }
        }
    }

}
