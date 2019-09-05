from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/2")
def view_template():
    print("Chau mundo!")
    return render_template("index.html")

@app.route("/3")
def view_template2():
    # Run the model with the file: _from_backend_with_love.csv to see if our model works! 
    # The computer-power was too little to load the whole data through the night. 
    # That is why we used _from_backend_with_love.csv at our presentation.
    # Process dataframe
    df = pd.read_csv("from_backend_with_love.csv")
    df['Expected Return'] = round(df['Expected Return'],2) 
    df['Reliability (RMSE)'] = round(df['Reliability (RMSE)'],2)

    name = request.args.get('name')
    print (name)

    return render_template("page2.html",a_name=name, tablecontent=df.iterrows())


if __name__ == "__main__":
    app.run(debug=True)

