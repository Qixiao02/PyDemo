from flask import Flask, jsonify, url_for, request, redirect
import config

app = Flask(__name__)
app.config.from_object(config)

books = [
    {'id': 1, "name": '三国演义'},
    {'id': 2, "name": '水浒传'},
    {'id': 3, "name": '红楼梦'},
    {'id': 4, "name": '西游记'},
]


@app.route('/')
def index():
    return {"username": "谭文彦"}


@app.route('/book/detail/<int:book_id>')
def book_detail(book_id):
    for book in books:
        if book_id == book['id']:
            return book
    return f"没有id为{book_id}的书！"


# url构造
@app.route('/book/list', methods=['Get'])
def book_list():
    for book in books:
        book['url'] = url_for('book_detail', book_id=book['id'])
    return jsonify(books)


@app.route('/profile')
def profile():
    # 参数传递的两种形式:
    # 1.作为url的组成部分:/book/1
    # 2.查询字符串:/book?id=1
    user_id = request.args.get("id")
    if user_id:
        return "用户个人中心"
    else:
        return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()
