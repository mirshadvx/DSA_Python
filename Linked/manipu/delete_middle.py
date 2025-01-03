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
    
    def get_list_len(self):
        current_node = self.head
        count = 0
        
        while current_node:
            current_node = current_node.next
            count += 1
        return count
            
    def delete_middle(self):
        length = self.get_list_len()
        middle_index = length // 2
        
        prev_node = None
        current = self.head
        for _ in range(middle_index):
            prev_node = current
            current = current.next
        
        if prev_node is not None:
            prev_node.next = current.next
            if current == self.tail:
                self.tail = prev_node
            
            
        
            
List = Linked_List()
List.append(100)
List.append(1)
List.append(2)
List.append(3)
List.append(10)
List.append(80)
List.display()
List.get_list_len()
List.delete_middle()
print()
List.display()

