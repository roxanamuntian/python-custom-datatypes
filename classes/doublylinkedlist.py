class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doublylinkedlist:
    def __init__(self):
        self.head = None

    def __print_forward__(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def __print_backward__(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data)
                n = n.prev

    def __insert_empty__(self, data):
        if self.head is None:
            newNode = node(data)
            self.head = newNode
        else:
            print ('The list is not empty')

    def __add_begin__(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def __add_end__(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = newNode
            newNode.prev = n


