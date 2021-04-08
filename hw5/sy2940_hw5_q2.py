from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.maximum = None

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, element):
        self.data.push((element, self.maximum))
        if self.maximum is None or element > self.maximum:
            self.maximum = element

    def top(self):
        if self.is_empty():
            raise Exception("maxStack is empty")
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("maxStack is empty")
        popedValue = self.data.pop()
        # support tuple or just one number
        if not popedValue[1] or popedValue[0] > popedValue[1]:
            self.maximum = popedValue[1]
        return popedValue[0]

    def max(self):
        if self.is_empty():
            raise Exception("maxStack is empty")
        return self.maximum
