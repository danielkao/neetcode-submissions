class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            return -1

        current = self.head
        for _ in range(i):
            current = current.next
        return current.val

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

        if self.tail is None:      # list was empty
            self.tail = node

        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)

        if self.tail is None:      # list was empty
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def remove(self, i: int) -> bool:
        if i < 0 or i >= self.size:
            return False

        if i == 0:
            self.head = self.head.next
            if self.head is None:      # list is now empty
                self.tail = None
            self.size -= 1
            return True

        prev = self.head
        for _ in range(i - 1):
            prev = prev.next

        target = prev.next
        prev.next = target.next

        if target is self.tail:        # removed the tail node
            self.tail = prev

        self.size -= 1
        return True

    def getValues(self) -> list:
        values = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.next
        return values