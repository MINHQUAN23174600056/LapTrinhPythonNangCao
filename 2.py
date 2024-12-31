import threading
import time

def download(name):
    print(f"Bắt đầu tải xuống: {name}")
    time.sleep(2)
    print(f"Tải xuống hoàn thành: {name}")

if __name__ == "__main__":
    threads = []
    files = ["File-1", "File-2", "File-3"]
    for file in files:
        thread = threading.Thread(target=download, args=(file,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("Tải xuống hoàn thành")