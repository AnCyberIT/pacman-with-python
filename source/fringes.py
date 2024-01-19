import heapq
class Queue:
    def __init__(self):
        self.items = list()
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.pop(0)
        
    def is_empty(self):
        return len(self.items) == 0
    
    def contain(self, item) : 
        return item in self.items 

class Stack:
    def __init__(self):
        self.items = list()
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def contain(self, item) : 
        return item in self.items 
    
class PriorityQueue:
    def __init__(self):
        self.items = list()
        
    def push(self, item, priority):
        heapq.heappush(self.items, (item, priority))
        
    def pop(self):
        return (heapq.heappop(self.items))
        
    def is_empty(self):
        return len(self.items) == 0
    def contain(self, item) : 
        return item in self.items 