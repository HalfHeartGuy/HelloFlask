from flask import Flask, render_template
print(__name__)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
def qwe():
    paragraph = "<p>Hallo Welt</p>"
    listVersions = ["Minecraft 1.0.0:18. November 2011","Minecraft Version 1.1: 12. January 2012","Minecraft Version 1.2: 1. March 2012"]
    server_response = render_template("start.html", gameName = "minecraft",gameVersions = listVersions)
    return server_response


@app.route("/minecraft1_0")
def minecraft1_0():
    paragraph = "<h1>minecraft 1.0</h1>"
    return paragraph + "<br>"+ "adventure update"



if __name__ == '__main__':
    app.run()


