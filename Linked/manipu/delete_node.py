class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data,end=' ')
            current_node = current_node.next
        print()
            
    def delete_node(self, node):
        current = self.head
        prev = None
        
        while current :
            if current.data == node:
                if prev is None:
                    self.head = current.next
                    if self.head is None:
                        self.tail
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                return
                        
            else:
                prev = current
                current = current.next
    
        
            
List = Linked_List()
List.append(100)
List.append(1)
List.append(2)
List.append(3)
List.append(10)
List.append(80)
List.display()
List.delete_node(10)
List.display()