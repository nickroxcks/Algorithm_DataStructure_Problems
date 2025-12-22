from typing import List

'''
My Solution:

Utilize a stack to keep track of past days awaiting to find a greater temperature
When we find a greater temperature, continue to pop items in the stack for where
the current temperature is greater

O(n) time
O(n) memory
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = []
        for idx, num in enumerate(temperatures):

            sol.append(0)

            while stack and stack[-1][0] < num:
                temp, oldindex = stack.pop()
                sol[oldindex] = idx - oldindex

            # ensure we ignore the last element as it is always zero
            if ((idx != len(temperatures) - 1) and temperatures[idx+1] > num):
                sol[idx] = 1
            else:
                stack.append((num,idx))

            idx+=1

        return sol