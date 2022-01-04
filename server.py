from flask import Flask
print(__name__)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
def qwe():
    paragraph = "<p>Hallo Welt</p>"
    return "Hello guys" + paragraph
@app.route("/minecraft1_0")
def minecraft1_0():
    paragraph = "<h1>minecraft 1.0</h1>"
    return paragraph + "<br>"+ "adventure update"



if __name__ == '__main__':
    app.run()


