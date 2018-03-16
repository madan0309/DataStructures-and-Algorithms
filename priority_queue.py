'''
Created on Jan 13, 2018

@author: kur4ve
'''
class Priority_Queue():
    def __init__(self):
        self.items = []
    
    def enque(self, item):
        if self.is_empty():
            self.items.append(item)
                  
    def deque(self):
        pass
    
    def first_crew(self):
        pass
        
    def is_empty(self):
        return self.items == []
    
(H, C, Q) = map(lambda x:int(x), raw_input().split())
print H, C, Q 
for i in range(C):
    height, start, end = map(lambda x:int(x), raw_input().split())
    