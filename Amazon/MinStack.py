class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__minimumAtIndex = []
        self.__stack = []
        self.__currentMin = float("inf")
    def push(self, x: int) -> None:
        self.__stack.append(x)
        self.__currentMin = min(self.__currentMin, x) 
        self.__minimumAtIndex.append(self.__currentMin)

    def pop(self) -> None:
        self.__stack.pop()
        self.__minimumAtIndex.pop()
        self.__currentMin =  self.__minimumAtIndex[-1] if self.__minimumAtIndex else float("inf")
        # print(self.)

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__currentMin
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
