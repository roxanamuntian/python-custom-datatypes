class node:
    def __init__(self, data):
        self.data = data
        self.ref = None

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
        if self.head is None:
            print("The linked list is empty")
        n = self.head
        while n is not None:
            if n.data == data:
                break
            n = n.ref
        if n is None:
            print('Value not inside the list')
        elif n.data == self.tail.data:
            newNode = node(value)
            self.tail.ref = newNode
            self.tail = newNode
        else:
            newNode = node(value)
            newNode.ref = n.ref
            n.ref = newNode

    def __insert_empty__(self, data):
        if self.head is None:
            newNode = node(data)
            self.head = newNode
            self.tail = newNode
        else:
            print('The linked list is not empty')

    def __delete_first__(self):
        if self.head is None:
            print('The linked list is empty')
        else:
            self.head = self.head.ref

    def __delete_last__(self):
        if self.head is None:
            print('The linked list is empty')
        elif self.head.ref is None:
            self.head = None
            self.tail = None
        else:
            n = self.head
            while n.ref.ref is not self.tail.ref:
                n = n.ref
            n.ref = None
            self.tail = n

    def __delete_by_value__(self, value):
        if self.head is None:
            print('The linked list is empty')
            return

        if self.head.data == value:
            self.head = self.head.ref
            return

        if self.head.ref is None and self.head.data == value:
            self.head = None
            self.tail = None
            return


        n = self.head
        while n.ref is not None:
            if n.ref.data == value:
                break
            n = n.ref

        if n.ref is None:
            print("Node was not found")
        else:
            n.ref = n.ref.ref
