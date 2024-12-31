import threading
import requests

# Hàm thực hiện yêu cầu HTTP
def fetch_url(url, results, index):
    try:
        response = requests.get(url)
        results[index] = (url, response.status_code, response.text[:100])  # chỉ lấy 100 ký tự đầu
    except Exception as e:
        results[index] = (url, None, str(e))  # Lưu lỗi nếu có
# Hàm gửi các yêu cầu HTTP đồng thời
def fetch_urls_concurrently(urls):
    threads = []
    results = [None] * len(urls)  # Danh sách để lưu kết quả
    for i, url in enumerate(urls):
        thread = threading.Thread(target=fetch_url, args=(url, results, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return results
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
]

# Thực hiện các yêu cầu HTTP
results = fetch_urls_concurrently(urls)
for url, status_code, content in results:
    print(f"URL: {url}")
    print(f"Status Code: {status_code}")
    print(f"Content: {content}")
    print("-" * 50)