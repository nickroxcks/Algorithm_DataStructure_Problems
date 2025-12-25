'''

My Solution:

Sort then utilize a stack to keep track of fleets.

Number of elements in the stack after iterating through the list is the solution

O(nlogn + n) time
O(n) memory

'''
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #O(nlogn) time + O(n) memory to sort and build the lists
        pairs = list(zip(position, speed))
        pairs.sort()   # sort by position ascending
        position_sorted, speed_sorted = zip(*pairs)
        position_sorted = list(position_sorted)
        speed_sorted = list(speed_sorted)
        stack = []

        index = len(position_sorted) - 1
        curr_min = None
        stack = []
        for pos in reversed(position_sorted):

            time = (target - pos) / speed_sorted[index]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            '''
            if not curr_min or time <= curr_min:
                curr_min = time
            else:
                curr_min = time
                sol +=1
            '''
            index -=1
        return len(stack)
