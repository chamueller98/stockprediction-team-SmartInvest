from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/2")
def view_template():
    print("Chau mundo!")
    return render_template("index.html")

@app.route("/3")
def view_template2():

    # Process dataframe
    df = pd.read_csv("from_backend_with_love.csv")
    df['Expected Return'] = round(df['Expected Return'],2) 
    df['Reliability (RMSE)'] = round(df['Reliability (RMSE)'],2)

    name = request.args.get('name')
    print (name)

    return render_template("page2.html",a_name=name, tablecontent=df.iterrows())


if __name__ == "__main__":
    app.run(debug=True)

