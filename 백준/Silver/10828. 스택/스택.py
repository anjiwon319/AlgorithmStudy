import sys
input = sys.stdin.readline


class Stack:
    
    data = []
    
    def __init__(self):
        self.data = []
    
    def top(self):
        if self.data:
            return self.data[-1]
        else:
            return -1
        
    def push(self, n):
        self.data.append(n)

    def pop(self):
        if self.data:
            return self.data.pop(-1)
        else:
            return -1
            
    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        if self.data:
            return 0
        else:
            return 1
        
        

stack = Stack()

numTestCases = int(input())


for i in range(numTestCases):
    order = input().split()
     
    if len(order) == 1:
        if order[0] == "pop":
            print(stack.pop())
        elif order[0] == "size":
            print(stack.size())
        elif order[0] == "top":
            print(stack.top())
        else:
            print(stack.isEmpty())
        
    else:
        if order[0] == "push":
            stack.push(order[1])
    