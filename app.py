from flask import Flask

app = Flask(__name__)

@app.route("/")
name = input("How may we call you? ")
def writename (name):
    result = ("We kindly welcome you " + name + " have a look at your personalized table.")
    return result
print (writename(name))




#code unten nur damit automatische Wiederholung und wir nicht jedesmal seite killen müssen sondern nur 
# refresh, funktioniert jedoch momentan leider nicht..

if __name__ == "__main__":
    app.run(debug=True)