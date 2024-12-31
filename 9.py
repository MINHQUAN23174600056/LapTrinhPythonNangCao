import threading
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(1)
    print(f"Exiting {name}")

if __name__ == "__main__":
    threads = []
    tasks = ["Google", "Yahoo", "Facebook"]

    for task_name in tasks:
        thread = threading.Thread(target=task, args=(task_name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Exiting Main Thread")