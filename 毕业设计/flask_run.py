from flask import *
import sqlite3
import os

app = Flask(__name__)

path = os.getcwd()
db = path + "\data\data.db"
print("数据库链接成功！")


def connect_db():
    return sqlite3.connect(db)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/db')
def data():
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select lowPrice,highPrice,avgPrice,pubDate from vegetables where pubDate >= ('2022-09-25 00:00:00')")
    rows = cur.fetchall()
    return render_template("vegetables.html", rows=rows)


@app.route('/test')
def test():
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cur1 = conn.cursor()
    cur1.execute("select lowPrice,highPrice,avgPrice from vegetables where prodName=('大白菜')")
    rows1 = cur1.fetchall()
    return render_template("test.html", rows=rows1)


if __name__ == '__main__':
    app.run(debug=True)
