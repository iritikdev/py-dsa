
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self) -> None:
        array = ""
        current = self.head
        while current:
            array += str(current.data) + " "
            current = current.next
        return array

    def isEmpty(self):
        return self.size == 0

    def add(self, item):
        node = Node(item)

        if self.isEmpty():
            self.head = self.tail = node

        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def remove(self):

        if self.head == None:
            print("Queue underflow")
            return

        if self.head == self.tail:
            self.head = self.tail = None

        second = self.head.next
        self.head = None
        self.head = second

        self.size -= 1

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        return self.head.data

    def length(self):
        print(self.size)
