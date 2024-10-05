from xml.dom import minidom
# Load XML file
doc = minidom.parse('CHUONG2\sample.xml')
# Lấy phần tử root (company)
root = doc.documentElement
# In ra tên công ty
company_name = root.getElementsByTagName("name")[0].firstChild.data
print("Company Name:", company_name)
# Lấy danh sách các staff
staffs = root.getElementsByTagName("staff")
# In ra thông tin từng staff
for staff in staffs:
    staff_id = staff.getAttribute("id")
    staff_name = staff.getElementsByTagName("name")[0].firstChild.data
    staff_salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Staff ID: {staff_id}, Name: {staff_name}, Salary: {staff_salary}")