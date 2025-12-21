'''
My Solution:

Utilize a second stack, which keeps track of all the minimum values encountered.
The idea is that if we pop() and it happens to be the min element, we don't want to waste
time then searching for the entire stack for the new minimum.
Instead, utilize a second stack so the next minimum value is just at the top of our second stack

O(1) time for all operations
O(n) memory for storing 2 stacks
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if self.minStack and val == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None


    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()