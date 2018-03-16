'''
Created on Jan 13, 2018

@author: kur4ve
'''

class Queue:
    def __init__(self):
        self.items = []
    
    def enque(self, item):
        self.items.insert(0, item)
        return len(self.items)
        
    def deque(self):
        if not self.is_empty():
            print self.items.pop(), len(self.items)
        else:
            return -1, 0
    
    def is_empty(self):
        return self.items == []

queue = Queue()
N = input()
for i in range(N):
    operation = raw_input().split()
    if operation[0] == 'E':
        print queue.enque(operation[1])
    else:
        queue.deque()