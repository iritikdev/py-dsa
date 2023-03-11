import ctypes


class Array:
    def __init__(self, capacity=1) -> None:
        self.capacity = capacity
        self.length = 0
        self.items = (ctypes.py_object * capacity)()

    def __str__(self) -> str:
        elements = "["
        for i in range(self.length):
            elements += str(self.items[i])
            if i != self.length - 1:
                elements += ", "
        elements += "]"
        return elements

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index >= 0 and index <= self.length - 1:
            return self.items[index]
        else:
            raise IndexError("given index out of range")

    def append(self, item):
        if self.length == self.capacity:
            self.capacity = self.capacity * 2
            array = (ctypes.py_object * self.capacity)()
            for i in range(self.length):
                array[i] = self.items[i]
            self.items = array

        self.items[self.length] = item
        self.length += 1

    def pop(self):
        if self.length <= 0:
            raise IndexError("pop from empty list")
        item = self.items[self.length - 1]
        self.items[self.length - 1] = 0
        self.length -= 1

        return item

    def clear(self):
        self.length = 0
        self.capacity = 1


array = Array(3)

array.append(10)
array.append(20.3)
array.append("hello")
array.append(True)

print(array)

print("Done")
