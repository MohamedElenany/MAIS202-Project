from flask import Flask, render_template, request, jsonify,redirect,url_for
import model_final

app = Flask(__name__)
prediction = 0

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/result')
def result():
    return render_template("result.html")

@app.route("/data" , methods=["POST","GET"])
def get_result():
    global prediction
    if request.method == 'POST':
        data = request.form.get("data")
        data = data.split(",")
        prediction = model_final.predict(data)
        #redirect("/result")
        return "1"
    else:
        if (prediction == 0):
            return "The patient is predicted to have no heart disease"
        else:
            return f"The patient is predicted to have stage {prediction} heart disease"
    return "1"

if __name__=="__main__":
    app.run(debug=True)
