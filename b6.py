class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size  
    def __del__(self):
        del self.stack
    def isEmpty(self):
        return len(self.stack) == 0
    def isFull(self):
        return len(self.stack) == self.max_size
    def push(self, item):
        if self.isFull():
            print("Ngăn xếp đã đầy!")
        else:
            self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử!")
            return None
        else:
            return self.stack.pop()
    def count(self):
        return len(self.stack)
    def print(self):
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung ngăn xếp:", self.stack)
    def print_stack(self):
        self.print()
my_stack = Stack(5)
my_stack.push(1.1)
my_stack.push(2.2)
my_stack.push(3.3)
my_stack.print()
print("Phần tử lấy ra:", my_stack.pop())
my_stack.print()
print("Số phần tử trên ngăn xếp:", my_stack.count())