# https://leetcode.com/problems/min-stack/submissions/

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# use two stacks
# push x to stack, and push the lesser of current min and x to min-stack
# pop from both


class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if not self.mins:
            self.mins.append(x)
        else:
            current_min = self.mins[-1]
            self.mins.append(min(x, current_min))

    def pop(self) -> None:
        if not len(self.stack):
            return

        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.mins[-1] if self.mins else None
