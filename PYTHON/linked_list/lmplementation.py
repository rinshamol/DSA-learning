# Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def insert_at_position(self,data,position):
        new_node = Node(data)
        if self.head is None:
            print("position not found")
            return
        temp = self.head
        for i in range(0,position-1):
            temp = temp.next
        new_node.next = temp.next.next
        temp.next = new_node
    def delete_start(self):
        if self.head is None:
            print("Empty")
            return
        self.head = self.head.next

ll = LinkedList()
ll.insert_start(12)
ll.insert_start(11)
ll.insert_start(10)
ll.print_ll()
ll.insert_at_end(9)
ll.print_ll()
ll.insert_at_position(33,2)
ll.print_ll()
ll.delete_start()
ll.print_ll()

