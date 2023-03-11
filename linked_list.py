class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node({str(self.value)})"

    def __repr__(self) -> str:
        return f"Node({str(self.value)})"


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        result = ""
        current = self.head
        while current:
            result += str(current.value) + " -> "
            current = current.next
        result += "None"
        return result

    def __repr__(self) -> str:
        result = ""
        current = self.head
        while current:
            result += str(current.value) + " -> "
            current = current.next
        result += "None"
        return result

    def isEmpty(self):
        return self.head == None

    def addLast(self, item):
        node = Node(item)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def addFirst(self, item):
        """Add item at first index"""
        node = Node(item)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def indexOf(self, item) -> int:
        index = 0
        current = self.head
        while current:
            if current.value == item:
                return index
            index += 1
            current = current.next
        return -1

    def contains(self, item) -> bool:
        """Return True if LinkedList object contains item"""
        current = self.head
        while current:
            if current.value == item:
                return True
            current = current.next
        return False

        "Return lenght of linkedList"
        return self.size

    def removeLast(self):
        # LinkedList is empty
        if self.isEmpty():
            raise ValueError

        # Have one element
        if self.head == self.tail:
            self.head = self.tail = None
            return

        current = self.head
        while current:
            if current.next == self.tail:
                break
            current = current.next
        current.next = None
        self.tail = current

        # decrement the size
        self.size -= 1

    def removeFirst(self):
        if self.isEmpty():
            raise ValueError

        if self.head == self.tail:
            self.head = self.tail = None
            return

        second = self.head.next
        self.head.next = None
        self.head = second

        self.size -= 1

    def remove(self, item):
        index = self.indexOf(item)
        if index == -1:
            raise ValueError("Item doesn't exist")
        if index == 0:
            self.removeFirst()
            return
        prev = None
        current = self.head
        for i in range(index):
            prev = current
            current = current.next
        prev.next = current.next
        del current, prev

    def toList(self):
        result = []
        current = self.head

        while current:
            result.append(current.value)
            current = current.next

        return result

    def reverse(self):
        self.tail = self.head
        c1 = None
        c2 = None
        current = self.head

        while current != None:
            c1 = c2
            c2 = current
            current = current.next

            c2.next = c1
        self.head = c2

    def getFirst(self):
        if self.size == 0:
            return
        return self.head.value

    def getLast(self):
        if self.size == 0:
            return
        return self.tail.value

    def getAt(self, index):
        counter = 0
        current = self.head
        if index < 0 or index >= self.size:
            return "Invalid index"
        while current:
            if counter == index:
                return current.value
            counter += 1
            current = current.next

    def sum(self):
        sum = 0
        current = self.head
        while current:
            sum += current.value
            current = current.next
        return sum

    def max(self):
        if self.isEmpty():
            return "List is empty"

        max = self.head.value
        current = self.head

        while current:
            if current.value > max:
                max = current.value
            current = current.next

        return max

    def moveToHeadSearch(self, key):
        prev = None
        curr = self.head

        while curr:
            if key == curr.value:
                prev.next = curr.next
                curr.next = self.head
                self.head = curr
            prev = curr
            curr = curr.next

    def insert(self, index, item):
        node = Node(item)
        # O(1)
        if index == 0:
            node.next = self.head
            self.head = node
            return

        current = self.head

        for i in range(index - 1):
            current = current.next

        node.next = current.next
        current.next = node

    def removeDuplicatesFromSortedList(self):
        current = self.head
        forward = self.head.next

        while forward:
            if current.value == forward.value:
                current.next = forward.next
                forward = current.next
            else:
                current = current.next
                forward = forward.next

    def oddEvenList(self):
        odd = LinkedList()
        even = LinkedList()
        while self.size > 0:
            val = self.getFirst()
            self.removeFirst()
            if val % 2:
                odd.addLast(val)
            else:
                even.addLast(val)
        odd.tail.next = even.head
        self.head = odd.head
        self.tail = even.tail
        self.size = odd.size + even.size

    def getMiddle(self):
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value
