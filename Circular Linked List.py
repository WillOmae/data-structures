# Date: 24th March 2020
# Wissenschaftler: Wilbur
# Description: Circular Linked List

# Applications - closed loop with equally-weighted items
# 1. OS switch between various running applications.
# 2. OS user Round-Robin time sharing mechanism.
# 3. Turn-based multiplayer games.
# Advantages
# 1. Entire list can be read from any node of the linked list.
# 2. Data demands a circular list
# 3. Address reference to previous node can easily be found unlike a single linked list.
# Disadvantages
# 1. More complex compared to singly linked lists.
# 2. Easy infinite loop situation.
# 3. No support for direct access of elements.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, data):
        element = Node(data)
        if self.isEmpty():
            self.head = element
            self.last = element
            self.head.next = self.last
            self.last.next = self.head
        else:
            self.last.next = element
            self.last = element
            self.last.next = self.head
        return self.last

    def traverse(self, start=None):
        if start is None:
            start = self.head
        if self.isEmpty():
            print("The list is empty")
            return
        else:
            current = start
            print("Nodes: ", end=" ")
            print(current.data, end=" ")
            while(current.next != start):
                current = current.next
                print(current.data, end=" ")

    def isEmpty(self):
        return self.head is None

    def search(self, data):
        if self.isEmpty():
            return None
        else:
            current = self.head
            if current.data is data:
                return current
            while(current.next != self.head):
                if current.data is data:
                    return current
                current = current.next

    def delete(self, element):
        if self.isEmpty():
            return
        else:
            prevEl = self.last
            current = self.head
            if current is element:
                nextEl = current.next
                prevEl.next = nextEl
                current = None
                return
            while(current.next != self.head):
                if current is element:
                    nextEl = current.next
                    prevEl.next = nextEl
                    current = None
                    return current
                prevEl = current
                current = current.next


cList = CircularLinkedList()
print("Just after initialisation:")
cList.traverse()
for i in range(1, 11):
    cList.append(i)
cList.traverse()
cList.traverse(cList.search(5))
cList.delete(cList.search(1))
cList.traverse(cList.search(3))
