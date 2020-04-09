# Date: 26th March 2020
# Wissenschaftler: Wilbur
# Description: Queue

# Advantages
# 1. Enqueue O(1)
# 2. Dequeue O(1)
# Disadvantages
# 1. Not inherently searchable
# 2. Inserting within the queue is not inherently allowed
# 3. Removal of elements is dependent on the removal of the prior element
# Applications
# 1. Buffers


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, data):
        element = Node(data)
        if self.isEmpty():
            self.head = element
            self.tail = element
            self.head.next = self.tail
        else:
            self.tail.next = element
            self.tail = element
            self.tail.next = None

    def peek(self):
        return self.head

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            element = self.head
            self.head = self.head.next
            return element


queue = Queue()
for i in range(1, 11):
    queue.enqueue(i)
print(queue.dequeue().data)
print(queue.dequeue().data)
print(queue.dequeue().data)
print(queue.dequeue().data)
print(queue.dequeue().data)
print(queue.dequeue().data)

print(queue.peek().data)
print(queue.peek().data)
print(queue.peek().data)
