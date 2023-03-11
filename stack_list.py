class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node({str(self.value)})"


class StackLinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self) -> str:
        result = '['
        current = self.first
        while (current):
            result += ('' if result == '[' else ", ") + str(current.value)
            current = current.next
        result += ']'
        return result

    def push(self, item):
        """ Add item at last index """
        node = Node(item)

        if self.size == 0:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

        self.size += 1

    def pop(self):
        # LinkedList is empty
        if self.size == 0:
            raise OverflowError

        # Have one element
        if self.first == self.last:
            self.first = self.last = None
            return

        current = self.first
        while current:
            if current.next == self.last:
                break
            current = current.next
        item = current.next.value
        current.next = None
        self.last = current

        # decrement the size
        self.size -= 1

        return item

    def top(self):
        if self.size == 0:
            return "Stack underflow"
        return self.last.value

    def length(self):
        print(self.size)
