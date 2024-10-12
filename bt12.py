import requests
#Lấy dữ liệu từ API
def fetch_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    return response.json()
#Hiển thị thông tin các bài post
def display_posts(posts):
    print(f"Tổng số bài post: {len(posts)}")
    for post in posts[:10]:  #Giới hạn hiển thị 10 bài post đầu tiên
        print(f"UserID: {post['userId']}, ID: {post['id']}, Title: {post['title']}")
#Chương trình chính
posts = fetch_posts()
display_posts(posts)