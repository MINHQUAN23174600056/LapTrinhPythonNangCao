import threading
import time

def process_resource(resource):
    print(f"Processing {resource}...")
    time.sleep(1)  # Mô phỏng thời gian xử lý tài nguyên
    print(f"Completed processing {resource}")

if __name__ == "__main__":
    resources = ["Resource-1", "Resource-2", "Resource-3", "Resource-4"]
    threads = []
    # Tạo và xử lý tài nguyên trên các luồng
    for resource in resources:
        thread = threading.Thread(target=process_resource, args=(resource,))
        threads.append(thread)
        thread.start()
    # Chờ các luồng hoàn thành
    for thread in threads:
        thread.join()
    print("All resources have been processed")