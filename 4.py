import threading

# Hàm tính giai thừa cho một khoảng giá trị
def factorial_range(start, end, result, index):
    partial_result = 1
    for i in range(start, end + 1):
        partial_result *= i
    result[index] = partial_result

# Hàm tính giai thừa sử dụng nhiều luồng
def parallel_factorial(n, num_threads=4):
    if n == 0 or n == 1:
        return 1
    # Chia khoảng giá trị thành các phần
    step = n // num_threads
    threads = []
    results = [1] * num_threads
    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i < num_threads - 1 else n
        thread = threading.Thread(target=factorial_range, args=(start, end, results, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    # Tính giai thừa bằng cách nhân tất cả các kết quả trung gian
    total = 1
    for res in results:
        total *= res
    return total
n = 10  # Giai thừa của 10
num_threads = 4
print(f"Giai thừa của {n} dùng {num_threads} luồng: {parallel_factorial(n, num_threads)}")