class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)
            
    def _insert(self, current, new_node):
        
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)
    
    
    def in_order(self, current):
        if current:
            self.in_order(current.left)
            print(current.data, end=' ')
            self.in_order(current.right)
            
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, current, value):
        if current is None:
            return False
        if current.data == value:
            return True

        if value < current.data:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)    
    
bst = BST()
bst.insert(50)
bst.insert(45)
bst.insert(55)
bst.insert(30)
bst.insert(100)
bst.insert(20)
bst.insert(75)
bst.in_order(bst.root)
print()
print(bst.search(30))
print(bst.search(234))
