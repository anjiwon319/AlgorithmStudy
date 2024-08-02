import sys
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, n):
        self.queue.append(n)
        
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return int(self.size() == 0)
    
    def getFirstElement(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]
    
    def getLastElement(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]
    
q = Queue()
nums_order = int(input())

for i in range(nums_order):
    order = input().rstrip()
    if len(order.split()) == 2:
        order, num = order.split()
        num = int(num)
        q.push(num)
        
    else:
        if order == "pop":
            print(q.pop())
        elif order == "size":
            print(q.size())
        elif order == "empty":
            print(q.isEmpty())
        elif order == "front":
            print(q.getFirstElement())
        elif order == "back":
            print(q.getLastElement())