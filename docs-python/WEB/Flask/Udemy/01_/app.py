from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<html>
<head>
<style>
h1 {
    font-family: SaxMono;
    font-size: 2em;
    background-color: lightgray;
    padding: .3em;
}
</style>
<title>Chaotic Page</title>
</head>
<body>
<h1>New Page</h1>
<div>
Satan exists
</body>
</html>
"""

@app.route("/fuck")
def fuck():
    return render_template("home.html", dow={"today": "Tuesday", "tomorrow": "Wednesday"})

@app.route("/route")
def hey():
    class Anjote:
        def __init__(self, name, age, gender):
            self.name = name
            self.age  = age
            self.gender = gender

    anja = Anjote("Felipe", 38, "Male")
    return render_template("home.html", dow={"today": "Tuesday", "tomorrow": "Wednesday"}, ob=anja)


@app.route("/amazing")
def amazing():
    lista = [
        "canabis",
        "wowow",
        "genti",
        "sei não, bro",
        "tem coisa"
    ]
    return render_template("manezote.html", lista=lista)

@app.template_filter("global_function")
def global_function(value, ends):
    return value + " " + ends