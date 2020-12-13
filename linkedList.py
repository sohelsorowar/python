


class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Singly_linked_list:
    def __init__(self):
        self.tail=None
        self.head=None
        self.count = 0
    
    def append_item(self, data):
        node =Node(data)
        if self.head:
            self.head.next = node
            self.head = node

        else:
            self.tail = node
            self.head = node
        self.count +=1

    def iterate_item(self):
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item =  current_item.next
            yield val

items = Singly_linked_list()
items.append_item('PHP')
items.append_item('python')
items.append_item('Java')   

print("Original list: ")
for val in items.iterate_item():
    print(val)

print("\n Size of the list: ",items.count)
       