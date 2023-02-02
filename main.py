from flask import Flask, render_template
import requests
from post import Post

blogs_api = "https://api.npoint.io/10a04cb38ca95cf9e01a"
response = requests.get(url=blogs_api)
blog_posts = response.json()
all_posts = []
for blog_post in blog_posts:
    all_posts.append(Post(blog_post["id"], blog_post["title"], blog_post["subtitle"], blog_post["body"]))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = all_posts)

@app.route("/blog/<int:id>")
def blog(id):
    requested_post = None
    for post in all_posts:
        if post.id == id:
            requested_post = post

    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)
