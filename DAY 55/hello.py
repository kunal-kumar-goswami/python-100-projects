from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
        '<p>Welcome!</p>'\
        '<img scr="<a href="https://www.picgifs.com/glitter-gifs/"><img src="https://www.picgifs.com/glitter-gifs/w/welcome/picgifs-welcome-2-566738.gif" border="0" /></a>"'
        

@app.route("/bye")
@make_bold
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello {name}, your are {number} years old!"



if __name__ == "__main__":
    app.run(debug=True )


