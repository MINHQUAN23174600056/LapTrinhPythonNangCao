import numpy as np
with open("CHUONG3/heights_1.txt", "r") as f:
    heights = [float(line.strip()) for line in f]
with open("CHUONG3/weights_1.txt", "r") as f:
    weights = [float(line.strip()) for line in f]
#1,2.Tạo numpy array từ list heights và weights
arr_height = np.array(heights)
arr_weight = np.array(weights)
print("Numpy array của chiều cao(heights):", arr_height)
print("Numpy array của cân nặng(weights):", arr_weight)
#3.Tạo arr_height_m dựa trên công thức arr_height * 0.0254
arr_height_m = arr_height * 0.0254
print("Chiều cao sau khi quy đổi sang m là:", arr_height_m)
#4.Tạo arr_weight_kg dựa trên công thức arr_weight * 0.453592
arr_weight_kg = arr_weight * 0.453592
print("Cân nặng sau khi quy đổi sang kg là:", arr_weight_kg)
#5.Tính BMI
arr_bmi = arr_weight_kg * (arr_height_m * arr_height_m)
print("Chỉ số BMI :", arr_bmi)
#6.Hiển thị giá trị cân nặng ở vị trí index 50
arr_weight_kg = arr_weight_kg[49]
print("Giá trị cân nặng ở vị trí index 50:",arr_weight_kg)
#7.Tạo arr_height_m_100
arr_height_m_100 = arr_height_m[99:109]
print("Giá trị chiều cao từ vị trí index 100 đến 110 :",arr_height_m_100)
#8.Cho viết cầu thủ bóng chày có bmi < 21 trong arr_bmi
bmi = arr_bmi < 21
print("Các cầu thủ bóng chày có bmi < 21:")
print(bmi)
# 9.Tính chiều cao , cân nặng trung bình
avg_height = np.mean(arr_height_m)
print(f"\nChiều cao trung bình: {avg_height:.2f} m")
avg_weight = np.mean(arr_weight_kg)
print(f"Cân nặng trung bình: {avg_weight:.2f} kg")
# 10.Tìm chiều cao , cân nặng lớn nhất
max_height = np.max(arr_height_m)
print(f"Chiều cao lớn nhất: {max_height:.2f} m")
max_weight = np.max(arr_weight_kg)
print(f"Cân nặng lớn nhất: {max_weight:.2f} kg")
# 11.Tìm chiều cao , cân nặng nhỏ nhất
min_height = np.min(arr_height_m)
print(f"Cân nặng nhỏ nhất: {min_height:.2f} kg")
min_weight = np.min(arr_weight_kg)
print(f"Cân nặng nhỏ nhất: {min_weight:.2f} kg")