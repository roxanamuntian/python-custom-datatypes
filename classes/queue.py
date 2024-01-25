class queue:
    def __init__(self):
        self.__items = []

    def __len__(self):
        return len(self.__items)

    def __enqueue__(self, item):
        if len(self) == 0:
            return Exception("Queue is empty. The enqueue operation cannot be perfromed.")
        return self.__items.append(item)

    def __dequeue__(self):
        if len(self) == 0:
            return Exception("Queue is empty. The dequeue operation cannot be perfromed.")
        return self.__items.pop(0)