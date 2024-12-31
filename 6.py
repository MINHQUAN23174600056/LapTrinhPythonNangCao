import threading

# Ngưỡng cho các số 
toi_thieu = 1
toi_da = 20
# Hàm in số chẵn theo thứ tự tăng dần
def print_even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Even: {num}")
even_thread = threading.Thread(target=print_even_numbers, args=(1, 20))  
even_thread.start()
even_thread.join()
# Hàm in số lẻ theo thứ tự tăng dần trong ngưỡng
def print_odd_numbers_in_threshold(lower, upper):
    for num in range(lower, upper + 1):
        if num % 2 != 0:
            print(f"Odd: {num}")
odd_thread = threading.Thread(target=print_odd_numbers_in_threshold, args=(toi_thieu, toi_da))
odd_thread.start()
odd_thread.join()