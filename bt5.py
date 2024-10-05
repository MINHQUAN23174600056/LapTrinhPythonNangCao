from xml.dom import minidom
# Load XML file
doc = minidom.parse('CHUONG2\sample.xml')
# Lấy tất cả các phần tử staff
staffs = doc.getElementsByTagName('staff')
# In ra tên của từng staff
for staff in staffs:
    name = staff.getElementsByTagName('name')[0].firstChild.data
    print("Staff Name:", name)