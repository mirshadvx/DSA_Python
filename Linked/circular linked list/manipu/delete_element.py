class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class circular_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def display(self):
        current = self.head
        
        while True:
            print(current.data, ' ')
            current = current.next
            if current == self.head:
                break
        print()
        
    def delete_node(self, node):
        current = self.head
        prev = None
        
        while current :
            if current.data == node:
                prev.next = current.next
                return
            else:
                prev = current
                current = current.next
            
        
        
cir = circular_linked_list()

cir.append(10)
cir.append(20)
cir.append(30)
cir.append(40)
cir.append(50)
cir.append(60)

cir.display()
cir.delete_node(40)
cir.display()