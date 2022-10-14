from flask import Flask, rander_template

app = Flask(__name__)


@app.route("/")
def hell_world():
    return "Hello World"

 
@app.route('/about')
def about():
    context = {
        'username': "周杰伦"
    }
    return rander_template("about.html", **context)


if __name__ == '__main__':
    app.run(debug=True)
