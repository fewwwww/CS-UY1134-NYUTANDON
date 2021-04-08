from ArrayStack import ArrayStack


class AlternativeQueue:
    def __init__(self):
        self.stackA = ArrayStack()
        self.stackB = ArrayStack()

    def __len__(self):
        return len(self.stackA) + len(self.stackB)

    def is_empty(self):
        return self.stackA.is_empty() and self.stackB.is_empty()

    def enqueue(self, item):
        self.stackA.push(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty")
        if self.stackB.is_empty():
            for counter in range(len(self.stackA)):
                self.stackB.push(self.stackA.pop())
        return self.stackB.pop()

    def first(self):
        if self.is_empty():
            raise Exception("queue is empty")
        if self.stackB.is_empty():
            for counter in range(len(self.stackA)):
                self.stackB.push(self.stackA.pop())
        return self.stackB.top()
