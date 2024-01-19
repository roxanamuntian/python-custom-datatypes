class stack:
    def __init__(self):
        self.__items = []

    def __len__(self):
        return len(self.__items)

    def __pop__(self):
        return self.__items.pop(0)
    