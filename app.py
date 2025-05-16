from flask import Flask, render_template, request
from utils import calculate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        op = request.form.get("operation")
        result = calculate(num1, num2, op)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
