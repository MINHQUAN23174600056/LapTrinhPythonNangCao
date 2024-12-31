import threading
def print_even_numbers():
    print("Số chẵn từ 30-50:")
    for number1 in range(30, 51):
        if number1 % 2 == 0:
            print(number1)
even_thread = threading.Thread(target=print_even_numbers)
even_thread.start()
even_thread.join()

def print_odd_numbers():
    print("Số lẻ từ 30-50:")
    for number2 in range(30, 51):
        if number2 % 2 != 0:
            print(number2)
odd_thread = threading.Thread(target=print_odd_numbers)
odd_thread.start()
odd_thread.join()