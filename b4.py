class Stack:
    def __init__(self, max_size):
        self.stack = []  
        self.max_size = max_size  
    #Hàm huỷ để giải phóng ngăn xếp
    def __del__(self):
        del self.stack
    #Phương thức kiểm tra ngăn xếp có trống hay không
    def isEmpty(self):
        return len(self.stack) == 0
    #Phương thức kiểm tra ngăn xếp có đầy hay không
    def isFull(self):
        return len(self.stack) == self.max_size
    #Phương thức thêm phần tử vào ngăn xếp 
    def push(self, item):
        if self.isFull():
            print("Ngăn xếp đã đầy")
        else:
            self.stack.append(item)
    #Phương thức lấy phần tử từ đỉnh ngăn xếp 
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử")
            return None
        else:
            return self.stack.pop()
    def print_stack(self):
        if self.isEmpty():
            print("Ngăn xếp trống")
        else:
            print("Ngăn xếp hiện tại:", self.stack)