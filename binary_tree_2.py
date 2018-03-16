'''
Created on Jan 13, 2018

@author: kur4ve
'''
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree():
    def insert(self, parent, item, direction):
        global all_nodes
        #print all_nodes
        for root in all_nodes:
            if root.data == parent:  
                if direction == 'L':
                    #print 'Inserting at Left'
                    root.left = Node(item)
                    all_nodes.append(root.left)
                else:
                    #print 'Inserting at Right'
                    root.right = Node(item)
                    all_nodes.append(root.right)
                break
    def get(self, path, root):
        parent = root
        for direction in path:
            if direction =="L":
                if parent.right:
                    parent = parent.right
                else:
                    print -1
                    return 0
            else:
                if parent.left:
                    parent = parent.left
                else:
                    return 0
        if parent:
            print parent.data
        else:
            print -1

    def find_path(self, item, root, path=""):
        #print path
        if root == None:
            return False
        elif root.data == item:
            #print "here ",path
            return path
        if self.find_path(item, root.left, path=path+"L"):
            path = self.find_path(item, root.left, path=path+"L")
            return path
        #self.find_path(item, root.left, path)
        elif self.find_path(item, root.right, path=path+"R"):
            path = self.find_path(item, root.right, path=path+"R")
            #print "path ",path
            return path
        #self.find_path(item, root.right, path)
        
all_nodes = []
root = Node('1')
all_nodes.append(root)
binary_tree = BinaryTree()
(N, Q) = map(lambda x: int(x), raw_input().split())
for i in range(N-1):
    (parent, item, direction) = raw_input().split()
    #print (parent, item, direction)
    binary_tree.insert(parent, item, direction)
for j in range(Q):
    x = raw_input()
    path = binary_tree.find_path(x, root, "")
    binary_tree.get(path, root) 