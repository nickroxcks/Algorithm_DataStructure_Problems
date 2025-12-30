from typing import List

'''
My initial solution

Linear scan using memory to store left and right maxes

O(n) time
O(n) memory

If we analyze an individual column in the graph, how do we determine how maby blue squares can be made(amount of water)?
The amount of water is limited by the minimum height between the left and right boundaries of that location.

So if the closest wall to the left has a height of 2, and the wall to the right has a height of 3, we can see that for
location i in the height graph, the amount of water that can be stored at that location is:

water = min(max_left, max_right) - height[i] >=0

We do not count negative water.


'''
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = [0] * len(height)
        left = 0
        right = len(height) - 1
        curr_max = 0
        for h in height:
            curr_max = max(h,curr_max)
            left_max.append(curr_max)
        curr_max = 0
        for h in reversed(height):
            curr_max = max(h,curr_max)
            right_max[right] = curr_max
            right-=1

        sol = 0
        for i, h in enumerate(height):
            sol = sol + max(0, min(left_max[i],right_max[i]) - h)
        return sol



