'''
My Solution:

Utilize a stack to keep track of order of operations
For every operation, add the result to the stack. That way we iterate
and build towards the final solution.

The final item in the stack is the evaluated expression

O(n) time for iterating the entire list
O(n) memory for utilizing a stack with worst case stack being the entire list
'''
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dic = {'*', '-','+','/'}
        for item in tokens:
            if item in dic:
                if stack:
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    if item == '*':
                        num3 = num1 * num2
                        stack.append(num3)
                    elif item == '-':
                        num3 = num1 - num2
                        stack.append(num3)
                    elif item == '+':
                        num3 = num1 + num2
                        stack.append(num3)
                    else:
                        # truncate the decimal portion
                        num3 = int(num1 / num2)
                        stack.append(num3)
            else:
                stack.append(item)

        # if we reach this point, there should be 1 item left in stack
        return int(stack[0])
