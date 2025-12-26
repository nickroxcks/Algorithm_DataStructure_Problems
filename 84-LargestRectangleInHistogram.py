'''
My Solution:
Linear scan with stack

If we look at the graphs we see that if a element can be scanned forward (next height is greater),
a potentially bigger rectangle could be formed.

So lets scan linearly and add our elements to a stack. The moment we find an element that is smaller then the top of the stack,
it means the previous stack element cannot be extended forward anymore to build a rectangle, thus we keep popping elements from the stack
if those elements heights are greater than the current analyzed height. For each popped element, calculate the areas from
that last element and then remove it from consideration.

The areas of an element in the stack are:
- The element height itself multiplied by 1
- The element height multiplied by the distance between that element and the furtherst element that is currently being scanned.

Each stack element will contain (index, height)

Keep in mind that if we pop elements from the stack, we have to consider that the current element we are analyzing could build a rectangle of width
up to that popped element, thus we should update the index of the current element to extend all the way back to that longest rectangle

This solution is best visualized with an illustration

O(n) time
O(n) memory

'''
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            new_index = index
            while stack and stack[-1][1] > height:
                curr_rec = stack.pop()
                curr_index, curr_height = curr_rec
                max_area = max(curr_height, max_area)
                max_area = max(curr_height * (index - curr_index), max_area)
                new_index = curr_index # grab the index the farthest rectangle is built with current height

            stack.append((new_index,height))

        last_index = len(heights) - 1
        while stack:
            curr_rec = stack.pop()
            curr_index, curr_height = curr_rec
            max_area = max(curr_height, max_area)
            max_area = max(curr_height * (last_index - curr_index + 1), max_area)

        return max_area
