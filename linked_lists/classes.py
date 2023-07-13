class LinkedListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None   

    def add(self, value):
        self.head = LinkedListNode(value, self.head)     
