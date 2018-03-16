'''
Created on Jan 12, 2018

@author: kur4ve
'''
class Stack:
    def __init__(self):
        self.items = []
        self.top = -1
    
    def is_empty(self):
        return self.items == []
    
    def top_item(self):
        return self.items[self.top]
    
    def push(self, item):
        self.items.append(item)
        self.top += 1
        return self.items[self.top-1]
        
    def pop(self):
        self.top -= 1
        return self.items.pop()
    
stack = Stack()
T = input()
for i in range(T):
    N, initial_player = raw_input().split()
    stack.push(initial_player)
    for j in range(int(N)):
        pass_given = raw_input().split()
        if pass_given[0] == 'P':
            prev_player = stack.push(pass_given[1])
        else:
            prev_player = stack.push(prev_player)
        #print 'prev_player ',prev_player
        #print stack.items
    print "Player",stack.top_item()