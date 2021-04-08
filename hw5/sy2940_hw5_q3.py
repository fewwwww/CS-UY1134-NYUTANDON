from ArrayDeque import ArrayDeque
from ArrayStack import ArrayStack


class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()

    def is_empty(self):
        return self.stack.is_empty() and self.deque.is_empty()

    def __len__(self):
        return len(self.stack) + len(self.deque)

    def push(self, element):
        self.deque.enqueue_last(element)
        if len(self.stack) < len(self.deque):
            self.stack.push(self.deque.dequeue_first())

    def top(self):
        if self.is_empty():
            raise Exception("midStack is empty")
        if self.deque.is_empty():
            return self.stack.top()
        return self.deque.last()

    def pop(self):
        if self.is_empty():
            raise Exception("midStack is empty")
        if len(self.stack) > len(self.deque):
            self.deque.enqueue_first(self.stack.pop())
        return self.deque.dequeue_last()

    def mid_push(self, element):
        if len(self.stack) > len(self.deque):
            self.deque.enqueue_first(element)
        else:
            self.stack.push(element)
