from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


@app.route("/")
def fun1():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def fun2():
    fname = request.form["full_name"]
    age = int(request.form["age"])
    bmi = float(request.form["bmi"])
    smoker = 1 if request.form["smoker"] == "yes" else 0
    my_model = pickle.load(open("model.pkl", "rb"))
    premium = round(my_model.predict([[age, bmi, smoker]])[0], 2)
    return "<h1>Hey {}, Your Predicted Premium is {} Rs.</h1>".format(fname, premium)


if __name__ == "__main__":
    # app.run(debug=True)
	app.run(host='0.0.0.0', port=8080)
