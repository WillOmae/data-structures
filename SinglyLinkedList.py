# Date: 24th March 2020
# Wissenschaftler: Wilbur
# Description: Singly Linked List

# Applications
# Advantages
# Disadvantages


class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        element = Element(None)
        self.head = None
        self.last = None

    def append(self, data):
        element = Element(data)
        if self.isEmpty():
            self.head = element
            self.last = element
            self.head.next = self.last
        else:
            self.last.next = element
            self.last = element
        self.last.next = None
        return self.last

    def display(self, start=None):
        if start is None:
            start = self.head
        if self.isEmpty():
            print("The list is empty")
            return
        else:
            current = start
            if current is not None:
                print("Elements: ", end=" ")
                print(current.data, end=" ")
                while(current.next is not None and current.next != start):
                    current = current.next
                    if current is not None:
                        print(current.data, end=" ")

    def isEmpty(self):
        return self.head is None

    def find(self, data):
        if self.isEmpty():
            return None
        else:
            current = self.head
            if current.data is data:
                return current
            while(current.next != self.head):
                if current is not None and current.data is data:
                    return current
                current = current.next


cList = SinglyLinkedList()
for i in range(1, 6):
    cList.append(i)
cList.display(cList.find(3))
