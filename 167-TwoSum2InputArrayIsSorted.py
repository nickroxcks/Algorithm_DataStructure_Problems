'''
My Solution:
Two pointers linear scan

Have left pointer p1 start from the beginning of array, and right pointer p2 start at end of the array.

Find the sums for where the pointers are pointing to, and either increase or decrease the pointers positions
such that they bring us closer to the target sum.

If the sums is larger than the target, it makes sense that since the array is sorted in increasing order, we want to move the right pointer
to the left as this will guarantee the next sum computed to be smaller, hopefully bringing us closer to finding the target sum.

Likewise if the sum is too small, we want to move the left pointer over to the right, as this guarantees the next computed sum to be bigger.

Since we are guaranteed one solution in the array, we are guaranteed that eventually the two pointers will reach a point where they the two sums.

Since we perform a linear scan with no memory, we find our complexity to be:

O(n) time
O(1) memory

===
Proof:
Let [...,a,b,c,...,d,e,f,...] be the input array that is sorted in ascending order and let the elements b and e be the exactly only solution.
Because we are moving the smaller index from left to right, and the larger index from right to left, at some point, one of the indices must reach either b or e.
Without loss of generality, suppose the smaller index reaches b first. At this time, the sum of these two elements must be greater than target.
Based on our algorithm, we will keep moving the larger index to the left until we reach the solution.
'''
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 1
        p2 = len(numbers)

        while p1 < p2:
            sum = numbers[p1-1] + numbers[p2-1]
            if sum == target:
                return [p1,p2]
            elif sum < target:
                p1+=1
            else:
                p2-=1
        return [None, None]