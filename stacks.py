class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
     
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    
def compute(s):
    stack = Stack()
    d = {'}': '{', ']': '[', ')': '('}
    #print s
    for brack in s:
        #print brack
        if brack in ['[', '(', '{']:
            stack.push(brack)
        else:
            try:
                current_close = stack.pop()
            except:
                return 'NO'
            if current_close != d[brack]:
                return 'NO'
    if stack.isEmpty():
        return 'YES'
    else:
        return 'NO'

N = int(input())
for i in range(N):
    s = raw_input()
    print compute(s)