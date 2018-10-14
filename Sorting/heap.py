'''
Created on Oct 14, 2018

@author: kon5329
'''
class Heap:
    def __init__(self):
        self.size = 0
        self.elements = []
    
    def __str__(self):
        string = " : ".join([str(i) for i in self.elements])
        
        return string
        
    def isEmpty(self):
        return self.size==0
    
    def getSize(self):
        return self.size
    
    def insert(self, element):
        self.size += 1
        self.elements.append(element)
        self._perculateUp()
        
    def _perculateUp(self):
        i = self.size - 1
        while(i>=0):
            parent = (i-1)//2
            if(parent>=0 and self.elements[parent] > self.elements[i]):
                self.elements[parent], self.elements[i] = self.elements[i], self.elements[parent]
            i = parent
    
    def _perculateDown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        lowest = i
        
        if(left<self.size and self.elements[i]>self.elements[left]):
            lowest = left
        
        if(right<self.size and self.elements[lowest]>self.elements[right]):
            lowest = right
            
        if(lowest != i):
            self.elements[lowest], self.elements[i] = self.elements[i], self.elements[lowest]
            self._perculateDown(lowest)
            
    def getMin(self):
        result = self.elements[0]
        self.elements[0], self.elements[self.size-1] = self.elements[self.size-1], self.elements[0]
        self.size -= 1
        del self.elements[self.size]
        self._perculateDown(0)
        return result
    
    def peekMin(self):
        return self.elements[0]
    
heap = Heap()
heap.insert(10)
heap.insert(8)
heap.insert(2)
heap.insert(20)
print(heap)
print(heap.getMin())
print(heap)
print(heap.getMin())
print(heap)
print(heap.getMin())
print(heap)
print(heap.getMin())
print(heap)