from flask import Flask, render_template, request
from trycsv import get_info
import math

app = Flask(__name__)


@app.route("/2")
def view_template():
    print("Chau mundo!")
    return render_template("index.html")

@app.route("/3")
def view_template2():
    name = request.args.get('name')
    print (get_info())
    print (name)

    return render_template("page2.html",a_name=name, tablecontent=get_info())


@app.route("/3")
def round_content():
    for content in tablecontent:
        round(content[3],2)
        round(content[4],2)
    return round_content()


if __name__ == "__main__":
    app.run(debug=True)

