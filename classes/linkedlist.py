from node import node

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __print_linked_list__(self):
        if self.head is None:
            print("The linkedlist is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def __add_begin__(self, data):
        newNode = node(data)
        if self.head is None:
            newNode.ref = self.head
            self.head = newNode
            self.tail = newNode
        else:
            newNode.ref = self.head
            self.head = newNode

    def __add_end__(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.ref = newNode
            self.tail = newNode

    def __add_after_node__(self, data, value):
        n = self.head
        while n is not None:
            if n.data == data:
                break
            n = n.ref
        if n is None:
            print('Value not inside the list')
        else:
            newNode = node(data)
            newNode.ref = n.ref
            n.ref = newNode




linkedList1 = linkedlist()
linkedList1.__add_begin__(10)
linkedList1.__add_begin__(12)
linkedList1.__add_end__(13)
linkedList1.__add_end__(15)
linkedList1.__add_after_node__(16, 100)

print(linkedList1.__print_linked_list__())