import __main__
class TSTNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.equal = None
        self.is_leaf = None

def _insert(node, x):
    if len(x) == 0:
        return node
    head = x[0]
    #If the root is None create new TST Node
    if node is None:
        node = TSTNode(head)
        #print("Node created", node.data)
    if head < node.data:
        node.left = _insert(node.left, x)
    elif head > node.data:
        node.right = _insert(node.right, x)
    else:
        if len(x[1:])==0:
            node.is_leaf = True
        else:
            node.equal = _insert(node.equal, x[1:])
    return node

def _search(node, x):
    if node is None or len(x)==0:
        return False
    #print(node.data, x)
    head = x[0]
    tail = x[1:]
    if head==node.data:
        if node.is_leaf or len(tail)==0:
            return node.equal
        return _search(node.equal, tail)
    elif head < node.data:
        return _search(node.left, x)
    else:
        return _search(node.right, x)

def _find_all_words(node, L, str=""): 
    #print(node.data, L, str)
    if node.data is None:
        return
    if node.is_leaf:
        L.append(str+node.data)
    if node.equal: 
        #print("Equal "+node.data)
        _find_all_words(node.equal, L, str+node.data)
    if node.left: 
        #print("Left "+node.data)
        _find_all_words(node.left, L, str)
    if node.right: 
        #print("Right "+node.data)
        _find_all_words(node.right, L, str)
    return L
def autocomplete(node, x):
    node = _search(node, x)
    suggested_words = []
    while(node):
        if node.data:
            pass
        
class TST:
    def __init__(self):
        self.root = None
        
    def append(self, word):
        self.root = _insert(self.root, word)
    
    def search(self, word):
        node = _search(self.root, word)
        if node:
            return "Word \'{}\' is in the TST".format(word)
        else:
            return "Word \'{}\' is Not in the TST".format(word)
    def find_all_words(self, word):
        node = _search(self.root, word)
        print("\nNode till the given word {} is {}".format(word, node))
        if node:
            return _find_all_words(node, [], word)
        else:
            return -1
    
if __name__ == "__main__":
    tree = TST()
    print(dir())
    fp = open('wordsEn.txt')
    words = fp.read().split('\n')
    fp.close()
    for line in words:
        tree.append(line.strip())
    tree.append('bat')
    tree.append('bats')
    tree.append('boat')
    tree.append('boats')   
    print(tree.search('bat'))
    print(tree.search('beat'))
    print(tree.search('baafdt'))
    print(tree.find_all_words('buff'))
    print(tree.find_all_words('banan'))