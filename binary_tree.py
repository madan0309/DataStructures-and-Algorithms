
# Write your code here
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
class Binary_Tree():
    def insert(self, path , root, item):
        parent = root
        for direction in path:
            if direction == 'L':
                if parent.left == None:
                    parent.left = Node(0)
                parent = parent.left
            else:
                if parent.right == None:
                    parent.right = Node(0)
                parent = parent.right
        parent.data = item
    #Maximum length between two nodes
    def diameter(self, root):
        global diameter
        if root is None:
            return 0 
        ldepth = self.diameter(root.left)
        rdepth = self.diameter(root.right)
        #print ldepth, rdepth, root.data
        if ldepth+rdepth+1 > diameter:
            diameter = ldepth + rdepth + 1
        return max(ldepth, rdepth)+1
            
diameter = 0
T,X = map(lambda x: int(x), raw_input().split())
root = Node(X)
btree = Binary_Tree()
for i in range(T-1):
    path = raw_input()
    item = input()
    btree.insert(path, root, item)

btree.diameter(root)
print diameter
