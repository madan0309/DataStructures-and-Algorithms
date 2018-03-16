'''
Created on Jan 12, 2018

@author: kur4ve
'''
class Stack:
    
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()


stack = Stack()
Q = int(input())
for i in range(Q):
    query = raw_input().split()
    if query[0] == '1':
        if not stack.is_empty():
            print(stack.pop())
        else:
            print 'No Food'
    elif query[0] == '2':
        stack.push(int(query[1]))