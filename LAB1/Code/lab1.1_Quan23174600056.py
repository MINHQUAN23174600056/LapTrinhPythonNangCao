import xml.etree.ElementTree as ET
class XMLReader: #Thiết kế xử lí dữ liệu từ 1 tệp
    def __init__(self, file_path): 
        self.file_path = file_path
        self.data = None #Thuộc tính
    def read_xml(self):
        tree = ET.parse(self.file_path) #phân tích tệp trả về đối tượng cây đặt là tree
        self.data = tree.getroot() #trích xuất gốc(root) của cây được lưu vào self.data
    def display_data(self): #Hiển thị nội dung
        if self.data: #Nếu dữ liệu ko rỗng, duyệt qua tất cả các thẻ con có tên là product(name,price,quantity)
            for product in self.data.findall('product'):
                name = product.find('name').text #thẻ 'name' có thuộc tính 'text'
                price = product.find('price').text 
                quantity = product.find('quantity').text
                print(f"Product: {name}, Price: {price}, Quantity: {quantity}")
# Sử dụng lớp XMLReader
path = 'LAB1/DATA//products.xml'
reader = XMLReader(path)
reader.read_xml()
reader.display_data()