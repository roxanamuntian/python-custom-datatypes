class stack:
    def __init__(self):
        self.__items = []

    def __len__(self):
        return len(self.__items)

    def __push__(self, item):
        return self.__items.append(item)

    def __pop__(self):
        if len(self) == 0:
            return Exception("Stack is empty. The pop operation cannot be perfromed.")
        return self.__items.pop(0)

    def __peek__(self):
        if len(self) == 0:
            return Exception('Stack is empty. The peek operation cannot be performed.')
        return self.__items[-1]
