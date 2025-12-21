'''
My Solution:

Utilize a stack to keep track of opening bracket sequence order and iterate through the input list one char at a time

O(n) time
O(n) memory for worst case the stack being the entire input list
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:

            # if we have an opening bracket, add to the stack
            if char in {'(', '[', '{'}:
                stack.append(char)

            # if we have a closing bracket, pop from the stack and see if the corresponding opening bracket is popped
            else:
                # handle stack is empty edge case
                if not stack:
                    return False
                x = stack.pop()
                if (char == ')' and x != '(') or (char == ']' and x !='[') or (char == '}' and x != '{'):
                    return False

        # only return true if the stack is empty
        if stack:
            return False
        else:
            return True