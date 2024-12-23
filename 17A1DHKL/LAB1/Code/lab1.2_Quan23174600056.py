import json
class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path      
        self.data = None
    def read_json(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file) #Đọc và chuyển đổi nội dung tệp thành đối tượng 'file'
    def display_data(self):
        if self.data: #Kiểm tra dữ liệu ko rỗng
            for user in self.data: #Duyệt qua từng đối tượng 
                                   #Sử dụng các khóa name,age,address để lấy thông tin
                                   #Sử dụng f-string để định dạng thông tin khi in ra 
                print(f"Name: {user['name']}, Age: {user['age']}, \
Address:{user['address']}")
# Sử dụng lớp JSONReader
path = 'LAB1/DATA//users.json'
reader = JSONReader(path)
reader.read_json()
reader.display_data()