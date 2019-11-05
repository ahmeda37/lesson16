from flask import Flask, render_template
import datetime

app = Flask(__name__)
year = datetime.datetime.now().year
name = "Abdul Ahmed"
cities = ["Edmonton", "Winnipeg", "Toronto"]
@app.route('/')
def index():
    return render_template("index.html",year=year,name=name)


@app.route('/about-me')
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(debug=True, port=4000)