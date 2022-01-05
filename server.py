from flask import Flask, render_template
print(__name__)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/minecraft/start")
def qwe():
    paragraph = "<p>Hallo Welt</p>"
    listVersions = ["Minecraft 1.0.0:18. November 2011","Minecraft Version 1.1: 12. January 2012","Minecraft Version 1.2: 1. March 2012"]
    server_response = render_template("start.html", gameName = "minecraft",gameVersions = listVersions)
    return server_response


@app.route("/minecraft/test")
def minecraft1_0():
    listVersions = ["Minecraft 1.0.0:18. November 2011", "Minecraft Version 1.1: 12. January 2012","Minecraft Version 1.2: 1. March 2012"]
    server_response = render_template("test.html", gameName = "minecraft",gameVersions = listVersions)

    return server_response



if __name__ == '__main__':
    app.run()


