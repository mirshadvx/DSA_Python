class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.dupli = []
        
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
            
    def delete_duplicate(self):
        current = self.head
        
        while current:
            checker = current.next
            while checker:
                if current.data == checker.data:
                    self.dupli.append(checker.data)
                checker = checker.next
            
            current = current.next
            
        self.delete_dupli()
        
    def delete_dupli(self):
        current = self.head
        pre = None
        
        while current:
            if current.data in self.dupli:
                if pre is None:
                    self.head = current.next
                    print(current.data)
                else:
                    pre.next = current.next
                current = current.next
            else:
                pre = current
                current = current.next
        
            
List = Linked_List()
List.append(100)
List.append(1)
List.append(2)
List.append(3)
List.append(1)
List.append(3)
List.append(10)
List.append(80)
List.append(100)
List.display()
print()
List.delete_duplicate()
List.display()