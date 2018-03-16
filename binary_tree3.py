'''
Created on Jan 13, 2018

@author: kur4ve
'''
class Node():
    def __init__(self, color=None, parent=None, index=None):
        self.color = color
        self.parent = parent
        self.child = []
        self.index = index

class Binary_Tree():
    def insert(self, color, parent, index):
        #print parent, color, index
        parent_obj = nodes[parent-1]
        #print parent_obj
        new_node = Node(color = color, parent = parent_obj, index = index)
        parent_obj.child.append(new_node)
        nodes.append(new_node)
        #print parent_obj.child
    
    def find_ancnsor(self, index):
        node = nodes[index-1]
        current_color = node.color
        #print "index, color ",node.index, node.color, node.parent
        parent = node.parent
        if parent:
            #print "parent ",node.parent, parent.color, parent.index, node
            while(parent.color != current_color):
                parent = parent.parent
                if parent == None:
                    return -1
            return parent.index
        return -1
        
bt = Binary_Tree()
N, C = map(lambda x:int(x), raw_input().split())
parents = map(lambda x:int(x), raw_input().split())
colors = map(lambda x:int(x), raw_input().split())
root = Node(parent=None, index=1, color=colors[0])
#print root
nodes = [root]
for i in range(1, N):
    bt.insert(parent = parents[i-1], color=colors[i], index=i+1)
for j in range(1, N+1):
    print bt.find_ancnsor(j),