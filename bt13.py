import requests
#Lấy dữ liệu từ API cho postId=1
def fetch_comments():
    url = 'https://jsonplaceholder.typicode.com/comments?postId=1'
    response = requests.get(url)
    return response.json()
#Hiển thị thông tin các bình luận
def display_comments(comments):
    print(f"Tổng số bình luận: {len(comments)}")
    for comment in comments[:3]:  #Giới hạn hiển thị 3 bình luận đầu tiên
        print(f"ID: {comment['id']}, Name: {comment['name']}, Body: {comment['body']}")
#Chương trình chính
comments = fetch_comments()
display_comments(comments)
