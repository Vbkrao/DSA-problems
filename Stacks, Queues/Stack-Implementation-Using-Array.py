class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.top = -1

    def push(self, num):
        if self.top < self.capacity - 1:
            self.top += 1
            self.arr[self.top] = num
            return 0
        else:
            return -1

    def pop(self):
        if self.top == -1:
            return -1
        else:
            value = self.arr[self.top]
            self.top -= 1
            return value

    def top_element(self):
        if self.top == -1:
            return -1
        else:
            return self.arr[self.top]

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1
