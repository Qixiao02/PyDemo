from flask import *
import sqlite3
import os
app = Flask(__name__)

path = os.getcwd()
db = path + "\data\data.db"
print(db)


def connect_db():
    return sqlite3.connect(db)


@app.route('/db')
def data():
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select prodName from vegetables where prodName=('大白菜')")
    rows = cur.fetchall()
    return render_template("vegetables.html", rows=rows)


@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

