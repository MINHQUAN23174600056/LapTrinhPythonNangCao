import threading

def calculate_sum(sublist, results, index):
    results[index] = sum(sublist)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    num_threads = 2
    chunk_size = len(numbers) // num_threads
    threads = []
    results = [0] * num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(numbers)
        sublist = numbers[start:end]
        thread = threading.Thread(target=calculate_sum, args=(sublist, results, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("Tổng:", sum(results))