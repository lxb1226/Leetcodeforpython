# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
        

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.stack.append(x)
        

#     def pop(self):
#         """
#         :rtype: void
#         """
#         self.stack.pop()
        

#     def top(self):
#         """
#         :rtype: int
#         """
#         self.stack[-1]
        

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         min = self.stack[0]
#         for value in self.stack:
#             if value < min:
#                 min = value
#         return  min

# from heapq import *

## heapq 堆
## 常见用法
# heap = []            # creates an empty heap
# heappush(heap, item) # pushes a new item on the heap
# item = heappop(heap) # pops the smallest item from the heap
# item = heap[0]       # smallest item on the heap without popping it
# heapify(x)           # transforms list into a heap, in-place, in linear time
# item = heapreplace(heap, item) # pops and returns smallest item, and adds
#                                # new item; the heap size is unchanged

# class MinStack(object):
#     def __init__(self):
#         self.lst = []
#         self.h = []

#     def push(self,x):
#         self.lst.append(x)
#         heappush(self.h,x)

#     def pop(self):
#         val = self.lst.pop()
#         self.h.remove(val)
#         heapify(self.h)
    
#     def top(self):
#         return self.lst[-1]
    
#     def getMin(self):
#         return self.h[0]

# 创建两个栈，一个用来记录当前位置的最小值


from collections import deque
class MinStack(object):
    def __init__(self):
        self.lst = deque()
        self.aux = deque()
    
    def push(self,x):
        self.lst.append(x)
        if not self.aux or self.aux[-1] > x:
            self.aux.append(x)
        else:
            self.aux.append(self.aux[-1])
    
    def pop(self):
        self.lst.pop()
        self.aux.pop()

    def top(self):
        return self.lst[-1]
    
    def getMin(self):
        return self.aux[-1]

        

if __name__ == "__main__":
    pass

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# print(param_3,param_4)