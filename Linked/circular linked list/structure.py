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
        
        
cir = circular_linked_list()

cir.append(10)
cir.append(20)
cir.append(30)
cir.append(40)

print("Circular Linked List:")
cir.display()

